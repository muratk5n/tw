import json
import xml.etree.ElementTree as ET, os, zipfile
from shapely.geometry import MultiPolygon, Polygon
from shapely.ops import unary_union

def get_merged_coordinates(xml_data, target_names):
    """Parses XML and returns a list of coordinate rings for target regions."""
    root = ET.fromstring(xml_data)

    ns = ""
    if root.tag.startswith("{"):
        ns = root.tag.split("}")[0] + "}"

    polygons = []

    for placemark in root.findall(f".//{ns}Placemark"):
        name_elem = placemark.find(f"{ns}name")

        if name_elem is not None and name_elem.text in target_names:
            coord_elems = placemark.findall(f".//{ns}coordinates")

            for coord_elem in coord_elems:
                if coord_elem.text:
                    raw_coords = coord_elem.text.strip().split()
                    parsed_points = []

                    for point_str in raw_coords:
                        parts = point_str.split(",")
                        if len(parts) >= 2:
                            lon = float(parts[0])
                            lat = float(parts[1])
                            parsed_points.append([lon, lat])

                    if len(parsed_points) >= 4:
                        polygons.append(Polygon(parsed_points))

    if not polygons:
        print(f"Warning: No matching polygons found for {target_names}")
        return []

    # Merge overlapping/adjacent polygons in this specific group
    combined_geom = unary_union(polygons)

    rings = []
    if isinstance(combined_geom, Polygon):
        rings.append([[c[0], c[1]] for c in combined_geom.exterior.coords])
    elif isinstance(combined_geom, MultiPolygon):
        for poly in combined_geom.geoms:
            rings.append([[c[0], c[1]] for c in poly.exterior.coords])

    return rings


# --- Example Usage ---

# Define your target regions structured by blocks
target_regions = {
    "TR": [
        "Armed Groups(SNA)-N.Aleppo [Operation Olive Branch]",
        "Armed Groups(SNA)-Raqqa [Operation Peace Spring]",
        "Armed Groups(SNA)-Hasakah [Operation Peace Spring]",
        "Armed Groups(SNA)-N Aleppo [Operation Eufrates Shield]"
    ],
    "SDF": [
        "Asayish/MOI deployment-Kobane",
        "YPG/Asayish-E. Hasakah",
        "YPG/Asayish-Hasakah",
        "Asayish/MOI deployment",
        "Asayish/MOI deployment-Ain Issa"
    ],
    "HTS": [
        "Armed Groups-E.Aleppo",
        "Armed Groups-W. Aleppo",
        "Armed Groups-S.Hasakah",
        "Armed Groups-S.Raqqa",
        "Armed Groups-Der al-zur ",
        "Armed Groups-E.Homs",
        "Armed Groups-N.Hama",
        "Armed Groups-Tartus",
        "Armed Groups-W. Homs",
        "Armed Groups-Idlib",
        "Armed Groups-N.W.Idlib",
        "Armed Groups-S.Idlib ",
        "Armed Groups-E Rif Damascus",
        "Armed Groups-Dar'a",
        "Armed Groups-Quneitra",
        "Armed Groups-S. Rif Damascus",
        "Armed Groups-W Rif Damascus",
        "Armed Groups-Latakia",
        "Polígono 57"
    ],
    "ISIS": [
        "ISIS presence"
    ],
    "DRUZE": [
        "Druze Armed Groups-Suwayda"
    ],
    "ISR": [
        "IDF Area of operations",
        "IDF-Occupied Golan",
        "IDF permanent presence"
    ]
}

# Read KMZ file
kmz_path = os.path.join(os.environ['HOME'], 'Downloads/Guerra Civil Siria.kmz')
with zipfile.ZipFile(kmz_path) as myzip:
    with myzip.open('doc.kml') as myfile:
        xml_content = myfile.read().decode('utf-8')                

# Process each block and store the results mapped to block names
output_data = {}
for block_name, regions in target_regions.items():
    output_data[block_name] = get_merged_coordinates(xml_content, regions)

# Save the block-mapped JSON structure to disk
output_filepath = "/tmp/out.json"
with open(output_filepath, "w", encoding="utf-8") as f:
    json.dump(output_data, f, indent=2)

print(f"Successfully saved structured blocks to {output_filepath}!")
