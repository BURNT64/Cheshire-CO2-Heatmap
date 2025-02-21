import geopandas as gpd
import matplotlib.pyplot as plt

# Load the GeoJSON file
geojson_path = "index.geojson.json"  # Ensure this is the correct filename
map_data = gpd.read_file(geojson_path)

# Plot the map
fig, ax = plt.subplots(figsize=(10, 8))
map_data.plot(ax=ax, color='lightgray', edgecolor='black')

# Add region names (if the file contains multiple regions with names)
if "name" in map_data.columns:
    for idx, row in map_data.iterrows():
        plt.annotate(text=row["name"],
                     xy=(row.geometry.centroid.x, row.geometry.centroid.y),
                     ha='center', fontsize=8, color='black')

plt.title("Cheshire West and Chester Boundary")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.show()