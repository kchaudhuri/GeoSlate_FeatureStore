"""
Handle Open Data
"""

import osmnx as ox
import geopandas as gpd

import osmnx as ox

def fetch_osm_features(place, tags, buffer=0, to_crs="EPSG:4326"):
    """
    Fetch features from OpenStreetMap using a place name and tag filters.

    Parameters:
        place (str): Location name (e.g., 'Pune, India', 'Berlin, Germany')
        tags (dict): OSM tags to filter, e.g., {"highway": True}, {"building": True}, {"landuse": "residential"}
        buffer (int): Optional buffer around place boundary in meters
        to_crs (str): Output CRS for result GeoDataFrame (default: WGS84)

    Returns:
        GeoDataFrame containing the filtered OSM geometries
    """
    try:
        print(f"Fetching OSM data for: {place} with tags {tags}")

        # Get place boundary polygon
        boundary = ox.geocode_to_gdf(place)

        if buffer > 0:
            boundary = boundary.to_crs(epsg=3857)  # Project to meters for buffering
            boundary["geometry"] = boundary.geometry.buffer(buffer)
            boundary = boundary.to_crs(to_crs)
        else:
            boundary = boundary.to_crs(to_crs)

        # Download OSM data within boundary
        gdf = ox.features_from_polygon(boundary.geometry.iloc[0], tags)

        if gdf.empty:
            print(f"No OSM features found for {tags} in {place}.")
        else:
            print(f"Fetched {len(gdf)} features from OSM.")

        return gdf.to_crs(to_crs)

    except Exception as e:
        print(f"Error fetching OSM data: {e}")
        raise


def fetch_city_roads(place, buffer=0, to_crs="EPSG:4326"):
    """
    Fetch all road features (LineStrings) within a city's administrative boundary using OSM.

    Parameters:
        place (str): City or region name (e.g., "Pune, India")
        buffer (int): Optional buffer around boundary in meters
        to_crs (str): Target CRS for output

    Returns:
        GeoDataFrame: Filtered GeoDataFrame containing only LineStrings or MultiLineStrings
    """
    tags = {"highway": True}  # fetch all types of roads

    print(f"Fetching roads for: {place}")

    roads = fetch_osm_features(place, tags=tags, buffer=buffer, to_crs=to_crs)

    # Filter to only LineString and MultiLineString geometries
    roads = roads[roads.geometry.type.isin(["LineString", "MultiLineString"])].copy()

    if roads.empty:
        print(f"No road geometries found for {place}.")
    else:
        print(f"Retrieved {len(roads)} road features for {place}.")

    return roads
