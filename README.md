# 🌍 FeatureStore

A modular and extensible **Feature Store for Geospatial Data** built with Python. It helps data scientists and ML engineers ingest, transform, and serve spatial features for machine learning models.

---

## ✨ Key Features

- 📥 **Ingestion** from shapefiles, GeoJSON, CSV, and OpenStreetMap
- 💾 **Save**: Save features as Parquet or Feather using a class-based interface
- 🔍 **Duplicate Detection**: Prevents saving previously stored geometries

---

## 🚀 Quickstart

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/FeatureStore.git
cd FeatureStore
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run test

```bash
python examples/simple_demo.py
```


## 🔧 Built With

- **Geospatial Tools**: `geopandas`, `shapely`
- **Hashing & Validation**: `hashlib`, `pandas`
- **Data Storage**: `parquet`, `feather`, `csv`

---

## 📈 Roadmap

- [x] Ingest and store vector and raster data
- [x] Class-based feature store with duplicate detection
- [ ] Feature engineering utilities
- [ ] Feature serving via FastAPI
- [ ] DVC integration for versioning
- [ ] Streamlit dashboard for feature exploration
- [ ] PyPI release

---

## 👨‍💻 Author

**Kaustubh Chaudhuri**  
ML Scientist | Geospatial AI
