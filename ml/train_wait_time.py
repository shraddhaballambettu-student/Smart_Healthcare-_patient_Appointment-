import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_absolute_error

from xgboost import XGBRegressor

df = pd.read_csv(
    "data/smart_hospital_appointment_dataset.csv"
)

target = df["waiting_time_minutes"]

categorical_cols = [
    "department",
    "appointment_type",
    "severity_level",
    "appointment_day"
]

encoders = {}

for col in categorical_cols:

    encoder = LabelEncoder()

    df[col] = encoder.fit_transform(
        df[col].astype(str)
    )

    encoders[col] = encoder

features = [
    "department",
    "appointment_type",
    "severity_level",
    "appointment_day",
    "doctor_experience_years"
]

X = df[features]

X_train,X_test,y_train,y_test = train_test_split(
    X,
    target,
    test_size=0.2,
    random_state=42
)

model = XGBRegressor(
    n_estimators=400,
    learning_rate=0.05,
    max_depth=6
)

model.fit(
    X_train,
    y_train
)

pred = model.predict(
    X_test
)

print(
    "MAE:",
    mean_absolute_error(
        y_test,
        pred
    )
)

joblib.dump(
    model,
    "models/wait_time_model.pkl"
)

joblib.dump(
    encoders,
    "models/wait_time_encoders.pkl"
)

print("Wait Time Model Saved")
