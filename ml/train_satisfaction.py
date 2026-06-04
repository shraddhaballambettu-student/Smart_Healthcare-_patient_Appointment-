import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

from lightgbm import LGBMRegressor

df = pd.read_csv(
    "data/smart_hospital_appointment_dataset.csv"
)

target = df[
    "patient_satisfaction_score"
]

from sklearn.preprocessing import LabelEncoder

categorical_cols = [
    "department",
    "severity_level"
]

for col in categorical_cols:

    encoder = LabelEncoder()

    df[col] = encoder.fit_transform(
        df[col].astype(str)
    )

features = [
    "age",
    "department",
    "severity_level",
    "waiting_time_minutes",
    "doctor_experience_years",
    "hospital_rating"
]

X = df[features]

X_train,X_test,y_train,y_test = train_test_split(
    X,
    target,
    test_size=0.2,
    random_state=42
)

model = LGBMRegressor(
    n_estimators=500
)

model.fit(
    X_train,
    y_train
)

pred = model.predict(
    X_test
)

print(
    mean_squared_error(
        y_test,
        pred
    )
)

joblib.dump(
    model,
    "models/satisfaction_model.pkl"
)

print(
    "Satisfaction Model Saved"
)
