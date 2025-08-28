import os
import geopandas as gpd
import pandas as pd
import hashlib
from shapely.geometry import Point, LineString, Polygon, MultiLineString
from shapely.geometry.base import BaseGeometry


class GeoFeatureStore:
    """
    GeoFeatureStore handles validating, saving and loading of processed geospatial features in efficient formats
    such as Parquet or Feather, with optional metadata logging.

    """
    def __init__(self, base_dir="data", registry_file="feature_registry.csv"):
        self.base_dir = base_dir
        os.makedirs(self.base_dir, exist_ok=True)
        self.registry_path = os.path.join(self.base_dir, registry_file)
        self._init_registry()

    def _init_registry(self):
        if not os.path.exists(self.registry_path):
            df = pd.DataFrame(columns=["hash", "filepath", "geom_type"])
            df.to_csv(self.registry_path, index=False)
        self.registry = pd.read_csv(self.registry_path)

    def _compute_geometry_hash(self, geometry: BaseGeometry):
        # Normalize and hash WKT
        wkt = geometry.wkt
        return hashlib.md5(wkt.encode()).hexdigest()

    def _check_duplicate(self, gdf: gpd.GeoDataFrame):
        for geom in gdf.geometry:
            geom_hash = self._compute_geometry_hash(geom)
            if geom_hash in self.registry["hash"].values:
                return True
        return False

    def save(self, gdf: gpd.GeoDataFrame, filename: str):
        if gdf.empty:
            raise ValueError("GeoDataFrame is empty and cannot be saved.")

        if not all(isinstance(geom, (Point, LineString, MultiLineString, Polygon)) for geom in gdf.geometry):
            raise ValueError("Unsupported geometry type. Only Point, LineString, MultiLineString, and Polygon are allowed.")

        if self._check_duplicate(gdf):
            raise ValueError("Duplicate geometries detected. This sample set has already been saved.")

        # Save to disk
        output_path = os.path.join(self.base_dir, filename)
        gdf.to_parquet(output_path)
        print(f"Saved GeoDataFrame to {output_path}")

        # Register hashes
        records = [{
            "hash": self._compute_geometry_hash(geom),
            "filepath": output_path,
            "geom_type": geom.geom_type
        } for geom in gdf.geometry]

        new_entries = pd.DataFrame(records)
        self.registry = pd.concat([self.registry, new_entries], ignore_index=True)
        self.registry.to_csv(self.registry_path, index=False)

    def load(self, filename: str) -> gpd.GeoDataFrame:
        filepath = os.path.join(self.base_dir, filename)
        gdf = gpd.read_parquet(filepath)
        print(f"Loaded GeoDataFrame from {filepath} | {len(gdf)} records")
        return gdf
