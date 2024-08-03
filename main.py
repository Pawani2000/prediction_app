import streamlit as st
from home import show_home
from prediction import show_prediction
from explore import show_explore

st.sidebar.title("Exploration")
page = st.sidebar.selectbox("Go to", ["Home", "Predict", "Explore"])

if page == "Home":
    show_home()
elif page == "Predict":
    show_prediction()
else:
    show_explore()