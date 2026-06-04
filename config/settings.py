import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = BASE_DIR / "data" / "smart_hospital_appointment_dataset.csv"

APP_NAME = "Smart Hospital Analytics"

PAGE_TITLE = "Smart Hospital Analytics Platform"

THEME_COLOR = "#0066CC"

MODEL_PATH = BASE_DIR / "models"

CACHE_TTL = 3600

RANDOM_STATE = 42
