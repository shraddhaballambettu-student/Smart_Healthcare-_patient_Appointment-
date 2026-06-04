import streamlit as st
import plotly.express as px
from src.loader import load_data

df = load_data()

st.title("Doctor Analytics")

doctor_perf = (
    df.groupby("doctor_experience_years")
    .agg({
        "patient_satisfaction_score":"mean",
        "total_bill":"sum"
    })
    .reset_index()
)

fig = px.scatter(
    doctor_perf,
    x="doctor_experience_years",
    y="patient_satisfaction_score",
    size="total_bill",
    title="Doctor Experience vs Satisfaction"
)

st.plotly_chart(
    fig,
    use_container_width=True
)
