import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from src.loader import load_data

df = load_data()

st.title("💰 Revenue Analytics")

total_revenue = df["total_bill"].sum()

avg_bill = df["total_bill"].mean()

medicine_revenue = df["medicine_cost"].sum()

test_revenue = df["test_cost"].sum()

c1,c2,c3,c4 = st.columns(4)

c1.metric("Total Revenue",f"${total_revenue:,.0f}")
c2.metric("Average Bill",f"${avg_bill:,.0f}")
c3.metric("Medicine Revenue",f"${medicine_revenue:,.0f}")
c4.metric("Test Revenue",f"${test_revenue:,.0f}")

st.divider()

department_revenue = (
    df.groupby("department")["total_bill"]
    .sum()
    .reset_index()
    .sort_values("total_bill",ascending=False)
)

fig = px.bar(
    department_revenue,
    x="department",
    y="total_bill",
    color="department",
    title="Department Revenue"
)

st.plotly_chart(fig,use_container_width=True)

city_revenue = (
    df.groupby("city")["total_bill"]
    .sum()
    .reset_index()
)

fig2 = px.treemap(
    city_revenue,
    path=["city"],
    values="total_bill",
    title="Revenue by City"
)

st.plotly_chart(fig2,use_container_width=True)

insurance = (
    df.groupby("insurance")["total_bill"]
    .sum()
    .reset_index()
)

fig3 = px.pie(
    insurance,
    names="insurance",
    values="total_bill",
    title="Insurance Revenue Share"
)

st.plotly_chart(fig3,use_container_width=True)
