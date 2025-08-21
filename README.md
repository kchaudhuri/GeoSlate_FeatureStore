# 🌍 FeatureStore

A modular and extensible **Feature Store for Geospatial Data** built with Python. It helps data scientists and ML engineers ingest, transform, and serve spatial features for machine learning models.

> 🚀 Ideal for use cases like urban planning, agriculture, disaster response, and retail location intelligence.

---

## ✨ Key Features

- 📥 **Ingestion** from shapefiles, GeoJSON, CSV, and OpenStreetMap
- 💾 **Save**: Save features as Parquet or Feather using a class-based interface
- 🔍 **Duplicate Detection**: Prevents saving previously stored geometries

---

## 📦 Project Structure

```bash
FeatureStore/
├── feature_store/
│   ├── ingest.py          # Ingest vector and raster data
│   ├── store.py           # Class-based feature store with registry and validation
│   └── utils.py           # Geometry, CRS, and helper functions
├── examples/
│   └── flood_risk_model.py
├── notebooks/
│   └── urban_landuse_classification.ipynb
├── data/                  # Sample or downloaded data
├── requirements.txt
└── README.md
```

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

## 📌 Why This Project?

Most ML pipelines underuse spatial data due to its complexity. This project simplifies that by building a reusable geospatial feature engineering framework — **ready for recruiters, research, and production**.

---

## 👨‍💻 Author

**Kaustubh Chaudhuri**  
ML Scientist | Geospatial AI