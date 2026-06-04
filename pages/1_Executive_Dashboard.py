import streamlit as st
from src.loader import load_data
from src.insights import generate_business_insights

df = load_data()

st.title("Executive Dashboard")

total_patients = df["patient_id"].nunique()

total_revenue = df["total_bill"].sum()

avg_wait = df["waiting_time_minutes"].mean()

avg_satisfaction = (
    df["patient_satisfaction_score"]
    .mean()
)

col1,col2,col3,col4 = st.columns(4)

col1.metric(
    "Patients",
    f"{total_patients:,}"
)

col2.metric(
    "Revenue",
    f"${total_revenue:,.0f}"
)

col3.metric(
    "Avg Wait",
    f"{avg_wait:.1f} mins"
)

col4.metric(
    "Satisfaction",
    f"{avg_satisfaction:.2f}"
)

st.divider()

st.subheader("AI Generated Insights")

for item in generate_business_insights(df):
    st.info(item)
