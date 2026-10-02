from datetime import datetime, timedelta, timezone
import json, math, os, rasterio
from PIL import Image
from rasterio.transform import from_bounds
from sentinelhub import (
    CRS,
    BBox,
    DataCollection,
    MimeType,
    MosaickingOrder,
    SentinelHubCatalog,
    SentinelHubRequest,
    SHConfig,
)


# ==========================================
# CONFIG (Copernicus Data Space Ecosystem)
# ==========================================
def _load_params(path="~/.twkeys.json"):
    with open(os.path.expanduser(path)) as f:
        return json.load(f)


def _cdse_url():
    return "https://sh.dataspace.copernicus.eu"


def _make_config():
    params = _load_params()
    config = SHConfig()
    config.sh_client_id = params["cdseid"]
    config.sh_client_secret = params["cdsesecret"]
    config.sh_base_url = _cdse_url()
    config.sh_token_url = (
        "https://identity.dataspace.copernicus.eu/auth/realms/CDSE/protocol/openid-connect/token"
    )
    return config


def _make_collection():
    return DataCollection.SENTINEL2_L2A.define_from(
        "s2l2a_cdse",
        service_url=_cdse_url(),
    )


def _evalscript():
    return """
//VERSION=3

function setup() {
    return {
        input: ["B04", "B03", "B02"],
        output: { bands: 3, sampleType: "AUTO" }
    };
}

function evaluatePixel(sample) {
    return [sample.B04 * 2.5, sample.B03 * 2.5, sample.B02 * 2.5];
}
"""


# ==========================================
# HELPERS
# ==========================================
def _get_bbox(lat, lon, radius):
    delta_lat = radius / 111320.0
    delta_lon = radius / (111320.0 * abs(math.cos(math.radians(lat))))
    return BBox(
        bbox=[lon - delta_lon, lat - delta_lat, lon + delta_lon, lat + delta_lat],
        crs=CRS.WGS84,
    )


def _find_scenes(config, collection, bbox, time_range):
    catalog = SentinelHubCatalog(config=config)
    results = catalog.search(
        collection,
        bbox=bbox,
        time=time_range,
        fields={
            "include": ["id", "properties.datetime", "properties.eo:cloud_cover"],
            "exclude": [],
        },
    )
    return sorted(results, key=lambda s: s["properties"]["datetime"])


def _save_outputs(image_array, bbox, outfile):
    """Write GeoTIFF and JPEG atomically (temp file + os.replace)."""
    tiff_path = f"{outfile}.tiff"
    jpg_path = f"{outfile}.jpg"
    tiff_tmp = f"{outfile}.tmp.tiff"
    jpg_tmp = f"{outfile}.tmp.jpg"

    height, width, bands = image_array.shape
    transform = from_bounds(bbox.min_x, bbox.min_y, bbox.max_x, bbox.max_y, width, height)

    with rasterio.open(
        tiff_tmp,
        "w",
        driver="GTiff",
        height=height,
        width=width,
        count=bands,
        dtype=image_array.dtype,
        crs="EPSG:4326",
        transform=transform,
    ) as dst:
        for i in range(bands):
            dst.write(image_array[:, :, i], i + 1)
    os.replace(tiff_tmp, tiff_path)

    Image.fromarray(image_array).save(jpg_tmp, quality=95, subsampling=0)
    os.replace(jpg_tmp, jpg_path)

    return tiff_path, jpg_path


# ==========================================
# MAIN API
# ==========================================
def fetch_image(
    lat,
    lon,
    zoom=1,
    outfile="/tmp/sentinel",
    day=None,
    out_pixels=512,    # output is always out_pixels x out_pixels
    base_res=10,       # meters per pixel at zoom 1 (Sentinel-2 native)
    zoom_factor=2,     # resolution multiplier per zoom level
):
    """
    Fetch a single-acquisition Sentinel-2 true-color image centered on lat/lon.

    zoom    : 1 = closest (10 m/px), each level doubles the ground width.
    outfile : base path without extension; writes <outfile>.tiff and <outfile>.jpg.
    day     : 'YYYY-MM-DD'. If None, uses the most recent acquisition in the last 30 days.

    Every pixel comes from one acquisition (no mixing of dates). If several
    scenes exist for the day, the one with the lowest cloud cover is used.
    Returns (tiff_path, jpg_path, scene_datetime_string), or None if no imagery.
    """
    config = _make_config()
    collection = _make_collection()

    resolution = base_res * zoom_factor ** (zoom - 1)
    radius_meters = out_pixels * resolution / 2
    bbox = _get_bbox(lat, lon, radius_meters)
    size = (out_pixels, out_pixels)
    print(
        f"Zoom {zoom}: {resolution} m/px, {radius_meters * 2 / 1000:.1f} km wide, "
        f"{size[0]}x{size[1]} pixels"
    )

    # --- pick one acquisition ---
    if day is not None:
        scenes = _find_scenes(config, collection, bbox, (day, day))
    else:
        now = datetime.now(timezone.utc)
        scenes = _find_scenes(config, collection, bbox, (now - timedelta(days=30), now))

    if not scenes:
        print("No imagery found for that location/date.")
        return None

    if day is not None:
        chosen = min(scenes, key=lambda s: s["properties"].get("eo:cloud_cover", 100))
    else:
        chosen = scenes[-1]  # most recent

    scene_str = chosen["properties"]["datetime"]
    scene_time = datetime.fromisoformat(scene_str.replace("Z", "+00:00"))
    print(f"Using scene {scene_str} (tile cloud cover {chosen['properties'].get('eo:cloud_cover')}%)")

    # a few-minute window pins the request to that single acquisition
    time_interval = (scene_time - timedelta(minutes=2), scene_time + timedelta(minutes=2))

    # --- request ---
    request = SentinelHubRequest(
        evalscript=_evalscript(),
        input_data=[
            SentinelHubRequest.input_data(
                data_collection=collection,
                time_interval=time_interval,
                mosaicking_order=MosaickingOrder.LEAST_CC,
                other_args={
                    "processing": {
                        "upsampling": "BILINEAR",
                        "downsampling": "BILINEAR",
                    }
                },
            )
        ],
        responses=[SentinelHubRequest.output_response("default", MimeType.TIFF)],
        bbox=bbox,
        size=size,
        config=config,
    )

    data = request.get_data()
    if not data:
        print("Request returned no data.")
        return None

    tiff_path, jpg_path = _save_outputs(data[0], bbox, outfile)
    print(f"Saved {tiff_path} and {jpg_path}")
    return tiff_path, jpg_path, scene_str
    
if __name__ == "__main__":
    fetch_image(48.8584, 2.2945, zoom=1, day="2026-09-21")
