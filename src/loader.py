import pandas as pd
import streamlit as st
from config.settings import DATA_PATH


@st.cache_data
def load_data():

    df = pd.read_csv(DATA_PATH)

    return df


@st.cache_data
def get_numeric_columns(df):

    return df.select_dtypes(
        include=["int64", "float64"]
    ).columns.tolist()


@st.cache_data
def get_categorical_columns(df):

    return df.select_dtypes(
        include=["object"]
    ).columns.tolist()
