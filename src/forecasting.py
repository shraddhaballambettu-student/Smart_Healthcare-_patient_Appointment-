from prophet import Prophet
import pandas as pd


def revenue_forecast(df):

    revenue = (
        df.groupby("appointment_month")
        ["total_bill"]
        .sum()
        .reset_index()
    )

    revenue.columns = [
        "ds",
        "y"
    ]

    revenue["ds"] = pd.to_datetime(
        revenue["ds"],
        errors="coerce"
    )

    model = Prophet()

    model.fit(revenue)

    future = model.make_future_dataframe(
        periods=12,
        freq="M"
    )

    forecast = model.predict(
        future
    )

    return model,forecast
