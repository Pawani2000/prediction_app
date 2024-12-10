import pandas as pd
import pickle as pk
import streamlit as st
import os

# Set page configuration
st.set_page_config(page_title="Car Price Prediction", page_icon="🚗", layout="wide")

# Load model function
def show_prediction():
    # Check if the model file exists
    if not os.path.exists('model.pkl'):
        st.error("Model file 'model.pkl' not found.")
        return
    
    model = pk.load(open('model.pkl', 'rb'))

    # Custom CSS for dark theme and styling
    st.markdown("""
        <style>
            .main {
                background-color: #2b3e50;
                color: #ffffff;
            }
            .sidebar .sidebar-content {
                background-color: #374a59;
                color: #ffffff;
            }
            h1, h2, h3 {
                color: #ffffff;
            }
            .stButton>button {
                background-color: #0066cc;
                color: white;
                font-size: 18px;
                height: 50px;
                width: 100%;
                border-radius: 8px;
            }
            .stButton>button:hover {
                background-color: #004a99;
                color: white;
            }
            .slider-text, .slider-value {
                color: #ffffff !important;
            }
            .prediction-card {
                padding: 1em;
                background-color: #374a59;
                border-radius: 10px;
                text-align: center;
                font-size: 24px;
            }
            .prediction-card h2 {
                font-size: 36px;
                margin-top: 10px;
                color: #4CAF50;
            }
        </style>
    """, unsafe_allow_html=True)

    st.title("🚗 Car Price Prediction Dashboard")

    # Load and preprocess car data
    try:
        cars_data = pd.read_csv('Cardetails.csv')
    except Exception as e:
        st.error("Failed to load car data.")
        return

    # Extract brand name from car model name
    def get_brand_name(car_name):
        return car_name.split(' ')[0].strip()
    cars_data['name'] = cars_data['name'].apply(get_brand_name)

    # User input fields
    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        name = st.selectbox('Car Brand', cars_data['name'].unique())
        year = st.slider('Manufacturing Year', 2017, 2024)
        fuel = st.selectbox('Fuel Type', cars_data['fuel'].unique())
        owner = st.selectbox('Owner Type', cars_data['owner'].unique())
    
    with col2:
        km_driven = st.slider('Kilometers Driven', 11, 200000)
        seller_type = st.selectbox('Seller Type', cars_data['seller_type'].unique())
        transmission = st.selectbox('Transmission Type', cars_data['transmission'].unique())
        seats = st.slider('Seats', 2, 10)

    with col3:
        mileage = st.slider('Mileage (km/l)', 10, 40)
        engine = st.slider('Engine Capacity (CC)', 900, 5000)
        max_power = st.slider('Max Power (bhp)', 20, 200)

    # Prediction button
    if st.button("Predict Car Price"):
        # Prepare input data
        input_data = pd.DataFrame([[name, year, km_driven, fuel, seller_type, transmission, owner, mileage, engine, max_power, seats]],
                                  columns=['name', 'year', 'km_driven', 'fuel', 'seller_type', 'transmission', 'owner', 'mileage', 'engine', 'max_power', 'seats'])

        # Map categorical features to numerical values as in the model training
        input_data['owner'].replace(['First Owner', 'Second Owner', 'Third Owner', 'Fourth & Above Owner', 'Test Drive Car'], [1, 2, 3, 4, 5], inplace=True)
        input_data['fuel'].replace(['Diesel', 'Petrol', 'LPG', 'CNG'], [1, 2, 3, 4], inplace=True)
        input_data['seller_type'].replace(['Individual', 'Dealer', 'Trustmark Dealer'], [1, 2, 3], inplace=True)
        input_data['transmission'].replace(['Manual', 'Automatic'], [1, 2], inplace=True)
        input_data['name'].replace(
            ['Maruti', 'Skoda', 'Honda', 'Hyundai', 'Toyota', 'Ford', 'Renault', 'Mahindra', 'Tata', 'Chevrolet',
             'Datsun', 'Jeep', 'Mercedes-Benz', 'Mitsubishi', 'Audi', 'Volkswagen', 'BMW', 'Nissan', 'Lexus', 'Jaguar',
             'Land', 'MG', 'Volvo', 'Daewoo', 'Kia', 'Fiat', 'Force', 'Ambassador', 'Ashok', 'Isuzu', 'Opel'],
            list(range(1, 32)), inplace=True)

        # Make prediction
        car_price = model.predict(input_data)[0]
        car_price = max(0, car_price)  # Ensure non-negative price

        # Display prediction
        st.markdown("<div class='prediction-card'>"
                    f"<h3>Estimated Car Price:</h3><h2>${car_price:,.2f}</h2>"
                    "</div>", unsafe_allow_html=True)

# Run the prediction app
show_prediction()
