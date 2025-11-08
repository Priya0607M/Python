import folium
from folium.plugins import HeatMap, Search
import pandas as pd

m = folium.Map(
    location=[16.5, 80.6], 
    zoom_start=7,
    tiles="CartoDB positron"
)

data = {
    "City": ["Vijayawada", "Visakhapatnam", "Anantapur", "Bhimavaram"],
    "Latitude": [16.5062, 17.6868, 14.6793, 16.5333],
    "Longitude": [80.6480, 83.2185, 78.6011, 81.5167],
    "Population": [1030000, 2000000, 267000, 142000]
}

df = pd.DataFrame(data)

marker_layer = folium.FeatureGroup(name="City Markers")

for _, row in df.iterrows():
    folium.Marker(
        [row["Latitude"], row["Longitude"]],
        popup=(
            f"<b>{row['City']}</b><br>"
            f"Population: {row['Population']}<br>"
            f"<a href='https://www.google.com/search?q={row['City']}+India' target='_blank'>Open in Google</a>"
        ),
        tooltip=row["City"],
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(marker_layer)

marker_layer.add_to(m)

heat_layer = folium.FeatureGroup(name="Population Heatmap")

heat_data = df[["Latitude", "Longitude", "Population"]].values.tolist()
HeatMap(heat_data, radius=25).add_to(heat_layer)

heat_layer.add_to(m)

Search(
    layer=marker_layer,
    search_label="name",
    placeholder="Search for a city..."
).add_to(m)

route_layer = folium.FeatureGroup(name="Route Example")

route_points = [
    [16.5062, 80.6480],
    [17.6868, 83.2185],
]

folium.PolyLine(
    route_points, 
    weight=5,
    tooltip="Route: Vijayawada → Visakhapatnam"
).add_to(route_layer)

route_layer.add_to(m)

folium.LayerControl().add_to(m)

m.save("Interactive_Map.html")
print("Professional Interactive Map created successfully!")