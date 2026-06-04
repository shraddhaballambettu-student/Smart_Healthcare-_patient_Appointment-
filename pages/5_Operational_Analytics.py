import streamlit as st
import plotly.express as px
from src.loader import load_data

df = load_data()

st.title("⚙ Operational Analytics")

avg_wait = df["waiting_time_minutes"].mean()

emergency_cases = (
    df["emergency_case"]
    .astype(str)
    .str.lower()
    .eq("yes")
    .sum()
)

completed = (
    df["appointment_status"]
    .astype(str)
    .str.lower()
    .eq("completed")
    .sum()
)

no_show = (
    df["appointment_status"]
    .astype(str)
    .str.lower()
    .eq("no show")
    .sum()
)

c1,c2,c3,c4 = st.columns(4)

c1.metric("Average Wait",f"{avg_wait:.1f} mins")
c2.metric("Emergency Cases",emergency_cases)
c3.metric("Completed",completed)
c4.metric("No Shows",no_show)

status = (
    df["appointment_status"]
    .value_counts()
    .reset_index()
)

fig = px.pie(
    status,
    names="appointment_status",
    values="count",
    title="Appointment Status"
)

st.plotly_chart(fig,use_container_width=True)

pivot = df.pivot_table(
    values="waiting_time_minutes",
    index="department",
    columns="appointment_day",
    aggfunc="mean"
)

fig2 = px.imshow(
    pivot,
    text_auto=True,
    title="Wait Time Heatmap"
)

st.plotly_chart(fig2,use_container_width=True)

severity = (
    df.groupby("severity_level")
    ["waiting_time_minutes"]
    .mean()
    .reset_index()
)

fig3 = px.bar(
    severity,
    x="severity_level",
    y="waiting_time_minutes",
    color="severity_level",
    title="Wait Time by Severity"
)

st.plotly_chart(fig3,use_container_width=True)
