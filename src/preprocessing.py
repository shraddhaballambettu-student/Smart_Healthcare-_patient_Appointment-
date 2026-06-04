import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder


def clean_data(df):

    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    return df


def encode_categorical(df):

    encoders = {}

    categorical_cols = df.select_dtypes(
        include=["object"]
    ).columns

    for col in categorical_cols:

        le = LabelEncoder()

        df[col] = le.fit_transform(
            df[col].astype(str)
        )

        encoders[col] = le

    return df, encoders


def create_features(df):

    df["revenue_per_patient"] = (
        df["total_bill"]
        /
        (df["previous_appointments"] + 1)
    )

    df["high_waiting_flag"] = (
        df["waiting_time_minutes"] > 60
    ).astype(int)

    return df
