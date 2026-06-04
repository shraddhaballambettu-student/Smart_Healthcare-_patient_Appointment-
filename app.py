import streamlit as st

st.set_page_config(
    page_title="Smart Hospital Analytics",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>

.main{
    background-color:#F5F7FA;
}

div[data-testid="metric-container"]{
    background:white;
    padding:15px;
    border-radius:12px;
    box-shadow:0px 2px 10px rgba(0,0,0,0.1);
}

</style>
""", unsafe_allow_html=True)

st.title("🏥 Smart Hospital Analytics Platform")

st.markdown("""
### Enterprise Healthcare Intelligence System

Use the sidebar to navigate.
""")
