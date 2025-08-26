"""
"""

import geopandas as gpd
import pandas as pd
# from shapely.geometry import Point, LineString, Polygon, MultiLineString


class GeoDataIngestor:
    '''
    GeoDataIngestor handles the ingestion of geospatial data from shapefiles and csv files.
    
    '''
    def __init__(self, default_crs="EPSG:4326"):
        self.default_crs = default_crs

    def load_vector_file(self, filepath):
        gdf = gpd.read_file(filepath)
        print(f"Loaded vector: {filepath}")
        if gdf.crs is None:
            gdf.set_crs(self.default_crs, inplace=True)
        else:
            gdf = gdf.to_crs(self.default_crs)
        return gdf
    
    def load_csv(filepath, lat_col="latitude", lon_col="longitude", crs=DEFAULT_CRS):
        try:
            df = pd.read_csv(filepath)
            geometry = [Point(xy) for xy in zip(df[lon_col], df[lat_col])]
            gdf = gpd.GeoDataFrame(df, geometry=geometry, crs=crs)
            return gdf
        except Exception as e:
            print(f"Error loading CSV with coordinates: {filepath} | {e}")
            raise

