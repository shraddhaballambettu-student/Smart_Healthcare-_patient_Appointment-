import streamlit as st
import plotly.express as px
from src.loader import load_data

df = load_data()

st.title("Patient Analytics")

fig = px.histogram(
    df,
    x="age",
    nbins=30,
    title="Patient Age Distribution"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

gender = (
    df["gender"]
    .value_counts()
    .reset_index()
)

fig2 = px.pie(
    gender,
    names="gender",
    values="count",
    title="Gender Distribution"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

fig3 = px.box(
    df,
    x="gender",
    y="bmi",
    title="BMI Distribution"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)
