"""

Project/
 └── data/
     ├── images/
     └── models/
         └── features (skimage).pkl/
         └── features (img2vec).pkl/
     └── labels.csv
 └── Feature_Extractors
     └── skimage_feature_extractor.py
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent

# Data
DATA_DIR = ROOT / "data"
IMAGES_DIR = DATA_DIR / "images"
MODELS_DIR = DATA_DIR / "models"
LABEL_CSV = DATA_DIR / "labels.csv"

# Feature Extractors
FEATURE_EXTRACTORS_DIR      = ROOT / "Feature_Extractors"

# Features
SKIMAGE_FEATURES_PATH = MODELS_DIR / "features (skimage).pkl"
IMG2VEC_FEATURES_PATH = MODELS_DIR / "features (img2vec).pkl"