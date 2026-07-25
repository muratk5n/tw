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

# Define your distinct target groups
target_regions_1 = [
    "S. Zaporizhia-Russian Armed Forces",
    "E. Zaporizhia-Russian Armed Forces",
    "Luhansk People's Republic (North Luhansk)",
    "Luhansk People's Republic (East Luhansk)",
    "Luhansk People's Republic (East Luhansk)",
    "Luhansk People's Republic (West Luhansk)",
    "Luhansk People's Republic (South Luhansk)",
    "Donetsk People's Republic (Central Donetsk)",
    "Donetsk People's Republic (East Donetsk)",
    "Donetsk People's Republic (Northern Donetsk)",
    "Donetsk People's Republic (North East Donetsk)",
    "Donetsk People's Republic (North West Donetsk)",
    "Donetsk People's Republic (West Donetsk)",
    "Donetsk People's Republic (South Donetsk)",
    "E.Kharkov-Russian Armed Forces",
    "N.E.Kharkov-Russian Armed Forces",
    "S.E. Dnipropetrovsk-Russian Armed Forces",
    "Kherson-Russian Armed Forces",
    "Nykolaiv-Russian Forces",
    "N.Kharkov-Russian Armed Forces",
    "Polígono 81",
    "Polígono 92",
    "Belgorod-Russian Armed Forces",
    "Polígono 78",
    "Kursk-Russian Armed Forces",
    "C. Sumy-Russian Armed Forces",
    "Sumy-Russian Armed Forces"
]

with zipfile.ZipFile(os.environ['HOME'] + '/Downloads/Guerra Ruso-Ucraniana 2022.kmz') as myzip:
    with myzip.open('doc.kml') as myfile:
        xml_content = myfile.read().decode('utf-8')                
    

# Gather all region groups into one master list
all_combined_groups = []

# List of all your region groups to process
all_targets = [target_regions_1]

for group in all_targets:
    group_rings = get_merged_coordinates(xml_content, group)
    # Add each coordinate ring directly to the top-level master array
    all_combined_groups.extend(group_rings)

# Save the unified master array to disk
output_filepath = "/tmp/out.json"
with open(output_filepath, "w", encoding="utf-8") as f:
    json.dump(all_combined_groups, f, indent=2)

print(f"Successfully saved combined regions to {output_filepath}!")
