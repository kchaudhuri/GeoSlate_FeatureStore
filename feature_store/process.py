"""
Spatial feature processing utilities for geospatial ML pipelines.
"""

import geopandas as gpd
import logging
from shapely.geometry import Point
from shapely.ops import nearest_points


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
