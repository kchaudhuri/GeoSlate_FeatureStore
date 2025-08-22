from feature_store import ingest, store

# Load a shapefile of administrative boundaries
shapefile_path = "data/india_districts.shp"
gdf = ingest.load_vector_file(shapefile_path)

# (Optional) Inspect
print(gdf.head())
print(gdf.crs)

# Save it for future feature engineering
store.save_geodataframe(gdf, output_path="artifacts/districts.parquet")

# (Optional) Load it back
loaded_gdf = store.load_geodataframe("artifacts/districts.parquet")
print(loaded_gdf.shape)