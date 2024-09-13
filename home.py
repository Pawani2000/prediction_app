import streamlit as st
import os


def show_home():
    st.title("Welcome to the Car Price Prediction App")
    
    st.markdown("""
    <div style="text-align: justify;">
    Use this app to predict car prices and explore car data.
    
    This interactive application is designed to assist you in predicting the market price of your car and exploring detailed car data. Whether you’re considering buying a Toyota Camry, selling a Honda Civic, or analyzing the market for a Ford Mustang, this app provides accurate price predictions and valuable insights. By inputting details like the car model, year, mileage, and other specifications, you can estimate the selling price with our advanced machine learning model. Additionally, explore trends and patterns in car data, such as average prices for different brands like Hyundai, BMW, or Mercedes-Benz, and discover the distribution of car prices across various models. This app is an essential tool for car enthusiasts, buyers, and sellers alike, offering a comprehensive view of the car market.
    </div>
    """, unsafe_allow_html=True)
    image_url = "https://drive.google.com/uc?export=download&id=16vTLJvaucpdgvLhvPtSr6OJ5jta78c5e"
    st.image(image_url, caption='Explore and Predict Car Prices', use_column_width=True)

if __name__ == "__main__":
    show_home()
