"""
Handle visualization
"""

import folium
import geopandas as gpd
# from folium import GeoJson
from folium.plugins import MarkerCluster


def mapify(gdf, map_tile="CartoDB positron", zoom=12):
    """
    Visualize a GeoDataFrame with points, lines, or polygons on an interactive map using folium.

    Parameters:
        gdf (GeoDataFrame): The input spatial data
        map_tile (str): The base map tileset (e.g., "OpenStreetMap", "CartoDB positron")
        zoom (int): Initial zoom level for the map

    Returns:
        folium.Map: An interactive folium map object
    """
    if gdf.empty:
        raise ValueError("The GeoDataFrame is empty and cannot be visualized.")

    # Center map on centroid of all geometries
    centroid = gdf.geometry.unary_union.centroid
    m = folium.Map(location=[centroid.y, centroid.x], tiles=map_tile, zoom_start=zoom)

    geom_types = gdf.geometry.type.unique().tolist()

    if "Point" in geom_types or "MultiPoint" in geom_types:
        cluster = MarkerCluster().add_to(m)
        for _, row in gdf.iterrows():
            if row.geometry.geom_type == "Point":
                folium.Marker(location=[row.geometry.y, row.geometry.x]).add_to(cluster)

    else:
        folium.GeoJson(
            gdf,
            name="geometry",
            tooltip=folium.GeoJsonTooltip(fields=gdf.columns.difference(['geometry']).tolist(), aliases=None)
        ).add_to(m)

    folium.LayerControl().add_to(m)
    return m
