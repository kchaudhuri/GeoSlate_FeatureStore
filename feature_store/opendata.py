"""
"""

import osmnx as ox
import geopandas as gpd


def fetch_city_roads(place: str, buffer: int = 0, to_crs: str = "EPSG:4326") -> gpd.GeoDataFrame:
    """
    Fetch all road features (LineStrings) within a city's administrative boundary using OSM.

    Parameters:
        place (str): City or region name (e.g., "Pune, India")
        buffer (int): Optional buffer around boundary in meters
        to_crs (str): Target CRS for output (default: WGS84)

    Returns:
        GeoDataFrame: Filtered GeoDataFrame containing only LineStrings or MultiLineStrings
    """
    tags = {"highway": True}  # fetch all types of roads

    logger.info(f"Fetching roads for: {place}")

    roads = fetch_osm_features(place, tags=tags, buffer=buffer, to_crs=to_crs)

    # Filter to only LineString and MultiLineString geometries
    roads = roads[roads.geometry.type.isin(["LineString", "MultiLineString"])].copy()

    if roads.empty:
        logger.warning(f"No road geometries found for {place}.")
    else:
        logger.info(f"Retrieved {len(roads)} road features for {place}.")

    return roads
