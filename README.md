# 🌍 GeoSlate FeatureStore

A modular and extensible **Feature Store for Geospatial Data** built with Python. It helps data scientists and ML engineers ingest, transform, and serve spatial features for machine learning models.

---

## ✨ Key Features

- 📥 **Ingestion** from shapefiles, GeoJSON, CSV, and OpenStreetMap
- 💾 **Save**: Save features as Parquet or Feather using a class-based interface
- 🔍 **Duplicate Detection**: Prevents saving previously stored geometries
- 📌 **Open data integration**: Added functionality to fetch Open Street Map data (as base maps)
- 📌 **Mapify the data**: Visualizes the location data

---

## 🚀 Quickstart

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/GeoSlate_FeatureStore.git
cd GeoSlate_FeatureStore
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run test

```bash
python -m examples.simple_demo
```


## 🔧 Built With

- **Geospatial Tools**: `geopandas`, `shapely`
- **Hashing & Validation**: `hashlib`, `pandas`
- **Data Storage**: `parquet`, `feather`, `csv`

---

## 📈 Roadmap

- [x] Ingest and store vector and raster data
- [x] Class-based feature store with duplicate detection
- [x] Open Data base map integration
- [x] Visualize location data
- [ ] Feature engineering utilities
- [ ] Feature serving via FastAPI
- [ ] DVC integration for versioning
- [ ] Streamlit dashboard for feature exploration
- [ ] PyPI release

---

## 👨‍💻 Author

**Kaustubh Chaudhuri**  
ML Scientist | Geospatial AI
