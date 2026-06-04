import streamlit as st
import plotly.express as px

from src.loader import load_data
from src.anomaly import detect_billing_anomalies

df = load_data()

st.title("🧠 Advanced Insights")

numeric = df.select_dtypes(
    include=["int64","float64"]
)

corr = numeric.corr()

fig = px.imshow(
    corr,
    text_auto=True,
    aspect="auto",
    title="Correlation Matrix"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

st.subheader(
    "Billing Anomaly Detection"
)

anomaly_df = detect_billing_anomalies(df)

anomalies = anomaly_df[
    anomaly_df["anomaly"] == -1
]

st.metric(
    "Anomalous Records",
    len(anomalies)
)

fig2 = px.scatter(
    anomaly_df,
    x="medicine_cost",
    y="total_bill",
    color="anomaly",
    title="Billing Outliers"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

st.dataframe(
    anomalies.head(50),
    use_container_width=True
)
