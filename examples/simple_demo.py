from feature_store import opendata

# import sys
# import os
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

print(opendata.fetch_city_roads('Thane, India').shape)