import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report
from xgboost import XGBClassifier

df = pd.read_csv(
    "data/smart_hospital_appointment_dataset.csv"
)

target = (
    df["appointment_status"]
    .astype(str)
    .str.lower()
    .eq("no show")
    .astype(int)
)

categorical_cols = [
    "gender",
    "city",
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
    "age",
    "gender",
    "city",
    "appointment_day",
    "appointment_month",
    "booking_to_appointment_days",
    "previous_appointments",
    "missed_previous_appointments",
    "waiting_time_minutes"
]

X = df[features]
y = target

X_train,X_test,y_train,y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = XGBClassifier(
    n_estimators=300,
    max_depth=5,
    learning_rate=0.05,
    random_state=42
)

model.fit(
    X_train,
    y_train
)

predictions = model.predict(
    X_test
)

print(
    classification_report(
        y_test,
        predictions
    )
)

joblib.dump(
    model,
    "models/no_show_model.pkl"
)

joblib.dump(
    encoders,
    "models/no_show_encoders.pkl"
)

print("No Show Model Saved")
