import streamlit as st
import numpy as np
import joblib

st.title("🤖 AI Predictions")



age = st.slider(
    "Patient Age",
    1,
    100,
    35
)

waiting = st.slider(
    "Waiting Time",
    0,
    300,
    25
)

previous = st.slider(
    "Previous Appointments",
    0,
    50,
    5
)

missed = st.slider(
    "Missed Appointments",
    0,
    20,
    1
)

rating = st.slider(
    "Hospital Rating",
    1,
    5,
    4
)

experience = st.slider(
    "Doctor Experience",
    1,
    40,
    10
)

if st.button("Predict"):

    prediction = model.predict_proba(
        [[
            age,
            waiting,
            previous,
            missed,
            rating,
            experience
        ]]
    )[0][1]

    st.metric(
        "No Show Probability",
        f"{prediction*100:.2f}%"
    )

    if prediction > 0.70:
        st.error("High Risk")
    elif prediction > 0.40:
        st.warning("Medium Risk")
    else:
        st.success("Low Risk")
