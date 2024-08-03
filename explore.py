import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def show_explore():
    st.title("Explore Car Data")
    
    # Load and display car data
    try:
        cars_data = pd.read_csv('Cardetails.csv')
        st.write(cars_data.head())
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return
    
    # Check if 'selling_price' column exists
    if 'selling_price' not in cars_data.columns:
        st.error("Column 'selling_price' does not exist in the data.")
        return

    # Ensure 'selling_price' is numeric
    if not pd.api.types.is_numeric_dtype(cars_data['selling_price']):
        st.error("Column 'selling_price' is not numeric.")
        return

    # Example: Distribution of car prices
    st.write("### Distribution of Car Prices")
    fig, ax = plt.subplots()
    ax.hist(cars_data['selling_price'], bins=20, edgecolor='black')
    ax.set_title('Distribution of Car Prices')
    ax.set_xlabel('Price')
    ax.set_ylabel('Frequency')
    st.pyplot(fig)

    # Example: Average price by brand
    st.write("### Average Price by Brand")
    try:
        avg_price_by_brand = cars_data.groupby('name')['selling_price'].mean().sort_values()
        st.bar_chart(avg_price_by_brand)
    except KeyError:
        st.error("Column 'name' does not exist in the data.")
    except Exception as e:
        st.error(f"Error generating bar chart: {e}")

    # Example: Price trend over time (assuming 'year' column exists)
    if 'year' in cars_data.columns:
        st.write("### Average Price by Year")
        try:
            avg_price_by_year = cars_data.groupby('year')['selling_price'].mean().sort_index()
            st.line_chart(avg_price_by_year)
        except Exception as e:
            st.error(f"Error generating line chart: {e}")
    else:
        st.warning("Column 'year' does not exist in the data.")

if __name__ == "__main__":
    show_explore()