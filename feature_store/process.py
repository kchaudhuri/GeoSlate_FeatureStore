"""
Spatial feature processing utilities for geospatial ML pipelines.
"""

import geopandas as gpd
import logging
from shapely.geometry import Point
from shapely.ops import nearest_points
from geopy.distance import geodesic


def create_buffer(gdf: gpd.GeoDataFrame, distance: float) -> gpd.GeoDataFrame:
    """
    Creates a buffer around each geometry in the GeoDataFrame.

    """
    gdf = gdf.copy()
    gdf["geometry"] = gdf.geometry.buffer(distance)
    print(f"✅ Buffered {len(gdf)} geometries by {distance} units.")
    return gdf


def calculate_distance_to_nearest(from_gdf: gpd.GeoDataFrame, to_gdf: gpd.GeoDataFrame, 
                                  from_id_col: str = None, to_id_col: str = None) -> gpd.GeoDataFrame:
    """
    Calculates the distance from each feature in `from_gdf` to the nearest feature in `to_gdf`.

    """
    from_gdf = from_gdf.copy()
    to_gdf = to_gdf.copy()

    to_sindex = to_gdf.sindex

    nearest_ids = []
    nearest_dists = []

    for geom in from_gdf.geometry:
        # Get nearby features using spatial index
        match_idx = list(to_sindex.nearest(geom.bounds, return_all=True)[0])
        possible_matches = to_gdf.iloc[match_idx]
        
        # Find the one with the minimum distance
        min_idx = possible_matches.geometry.distance(geom).idxmin()
        nearest = to_gdf.loc[min_idx]

        nearest_ids.append(nearest[to_id_col] if to_id_col else min_idx)
        nearest_dists.append(geom.distance(nearest.geometry))

    from_gdf["nearest_dist"] = nearest_dists
    if to_id_col:
        from_gdf["nearest_id"] = nearest_ids

    print(f"Calculated distances to nearest features for {len(from_gdf)} geometries.")
    return from_gdf

def measure_distance(point1: tuple, point2: tuple, unit: str = "km") -> float:
    """
    Measure the geodesic distance between two geographic coordinates.


    Parameters:
        point1 (tuple): (latitude, longitude) of the first point
        point2 (tuple): (latitude, longitude) of the second point
        unit (str): Unit of distance ("km", "m", "mi")


    Returns:
        float: Distance between the two points in specified units
    """
    distance_km = geodesic(point1, point2).kilometers
    if unit == "m":
        return distance_km * 1000
    elif unit == "mi":
        return distance_km * 0.621371
    return distance_km

# def spatial_join()

# def add_area_and_perimeter()

# def extract_zonal_stats()
