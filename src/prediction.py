import joblib
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def train_no_show_model(df):

    target = (
        df["appointment_status"]
        .astype(str)
        .str.lower()
        .eq("no show")
        .astype(int)
    )

    features = [
        "age",
        "waiting_time_minutes",
        "previous_appointments",
        "missed_previous_appointments",
        "hospital_rating",
        "doctor_experience_years"
    ]

    X = df[features]

    X_train,X_test,y_train,y_test = train_test_split(
        X,
        target,
        test_size=0.2,
        random_state=42
    )

    model = RandomForestClassifier(
        n_estimators=300,
        random_state=42
    )

    model.fit(X_train,y_train)

    predictions = model.predict(X_test)

    score = accuracy_score(
        y_test,
        predictions
    )

    joblib.dump(
        model,
        "models/no_show_model.pkl"
    )

    return score


def load_model():

    return joblib.load(
        "models/no_show_model.pkl"
    )
