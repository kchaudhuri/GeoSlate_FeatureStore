from feature_store import opendata
from feature_store import store
from feature_store import visualize

# import sys
# import os
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

sample_area = opendata.fetch_city_roads("Thane, India")
print(sample_area.shape)

# Instantiate datastore object
datastore = store.GeoFeatureStore()

# Save the new locations
# datastore.save(sample_area, "Thane_India")

# Load location dataxx
gdf = datastore.load("Thane_India")
print(gdf.head())

map = visualize.mapify(gdf)
map.save("data/Sample.html")

