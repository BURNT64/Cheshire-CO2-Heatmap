# Cheshire West & Chester CO₂ Emissions Map

This project visualizes CO₂ emissions across the Cheshire West and Chester region using Python, GeoPandas, and Matplotlib. It was developed as part of a university dissertation focused on sustainable design, public engagement, and the use of data science to reduce regional carbon emissions.

## About the Project

The goal of this project is to transform local environmental data into a clear, accessible visual format to raise public awareness and support decision-making. A sector-based heatmap is created from a GeoJSON boundary file, with labels positioned using centroid calculations for readability.

This script was integrated into a mobile prototype (designed in Figma) that displays carbon data and promotes climate-friendly behavior through intuitive UX/UI design.

## Technologies Used

- [Python](https://www.python.org/)
- [GeoPandas](https://geopandas.org/)
- [Matplotlib](https://matplotlib.org/)
- GeoJSON (for geographic boundary data)

## Files

- index.geojson.json: Boundary data for Cheshire West and Chester
- map_script.py: Python script that generates the CO₂ emissions heatmap

## 🗺️ Features

- Visualizes geographic boundaries of Cheshire West and Chester
- Annotates each region using centroid coordinates
- Uses color-coded map layers to simulate CO₂ emission zones (e.g., traffic-light color scheme)
- Fully customizable for future real-time emissions data integration

##  How to Use

1. **Clone the repository**
   git clone https://github.com/BURNT64/Cheshire-West---Chester-Map-with-Python.git
   cd Cheshire-West---Chester-Map-with-Python
   
2. **Install dependencies**
  Ensure you have Python installed and run:
  pip install geopandas matplotlib

3.  **Run the script**
  python map_script.py

## Reference to data
Copy the link below into your broswer of choice to access the data used in this script

https://digital-land.github.io/organisation/local-authority-eng/CHW/
