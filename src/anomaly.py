from sklearn.ensemble import IsolationForest


def detect_billing_anomalies(df):

    features = df[
        [
            "medicine_cost",
            "test_cost",
            "total_bill"
        ]
    ]

    model = IsolationForest(
        contamination=0.02,
        random_state=42
    )

    df["anomaly"] = model.fit_predict(
        features
    )

    return df
