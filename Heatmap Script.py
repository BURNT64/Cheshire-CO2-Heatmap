import geopandas as gpd  # Import GeoPandas for working with geospatial data
import matplotlib.pyplot as plt  # Import Matplotlib for plotting the map

# Load the GeoJSON file containing boundary data for Cheshire West and Chester
geojson_path = "index.geojson.json"  # Make sure the filename is correct and located in the working directory
map_data = gpd.read_file(geojson_path)  # Read the GeoJSON file into a GeoDataFrame

# Create a figure and axis for plotting the map
fig, ax = plt.subplots(figsize=(10, 8))  # Set the figure size for better visibility

# Plot the map data onto the axis
map_data.plot(ax=ax, color='lightgray', edgecolor='black')  # Fill the regions with light gray and outline with black

# Optional: Annotate the map with region names if the GeoJSON contains a "name" field
if "name" in map_data.columns:
    for idx, row in map_data.iterrows():
        plt.annotate(
            text=row["name"],  # The name of the region
            xy=(row.geometry.centroid.x, row.geometry.centroid.y),  # Place the label at the region's center
            ha='center', fontsize=8, color='black'  # Style the text
        )

# Add map title and axis labels for context
plt.title("Cheshire West and Chester Boundary")
plt.xlabel("Longitude")
plt.ylabel("Latitude")

# Display the final map
plt.show()
