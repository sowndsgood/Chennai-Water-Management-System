import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st




# Function to load sample water consumption data (replace with your actual data loading logic)
def load_water_data():
    # Sample water consumption data (replace with your actual data)
    data = {
        'Date': pd.date_range(start='2022-01-01', end='2022-12-31', freq='D'),
        'Water_Consumption': np.random.randint(10, 100, 365)  # Random daily water consumption values
    }
    df = pd.DataFrame(data)
    return df

# Function to simulate monthly water consumption analytics
def analyze_monthly_water_consumption(df, month):
    st.header(f"Monthly Water Consumption Analytics - {month}")

    # Filter data for the selected month
    df['Month'] = df['Date'].dt.strftime('%B')
    monthly_data = df[df['Month'] == month]

    # Identify dates where water consumption exceeds 90 gallons
    high_consumption_dates = monthly_data[monthly_data['Water_Consumption'] > 90]['Date']

    # Plot daily water consumption trend for the selected month
    fig, ax = plt.subplots()
    ax.plot(monthly_data['Date'], monthly_data['Water_Consumption'], marker='o', linestyle='-', label='Daily Water Consumption')
    plt.xlabel('Date')
    plt.ylabel('Water Consumption')
    plt.title(f'Daily Water Consumption Trend for {month}')
    plt.axhline(y=85, color='r', linestyle='--', label='Threshold (85 gallons)')
    plt.legend()

    # Highlight dates where water consumption exceeds 90 gallons
    for date in high_consumption_dates:
        ax.axvline(x=date, color='orange', linestyle='--', alpha=0.5)  # Highlight high consumption dates with orange dashed lines

    plt.xticks(rotation=45, ha='right')
    st.pyplot(fig)

    # Display summary statistics for the selected month
    st.subheader("Summary Statistics")
    st.write(monthly_data.describe())

    # Display dates where water consumption exceeds 90 gallons
    if not high_consumption_dates.empty:
        st.subheader("Dates with Water Consumption Exceeding 90 Gallons")
        st.write(high_consumption_dates)
    else:
        st.write("No dates with water consumption exceeding 90 gallons.")



# Function to display water conservation tips
def display_water_conservation_tips():
    st.header("Water Conservation Tips")
    st.write("Here are some tips to help you conserve water:")

    tips = [
        "Fix leaky faucets and pipes promptly.",
        "Take shorter showers.",
        "Install water-saving devices such as low-flow showerheads and toilets.",
        "Water your lawn and garden during the early morning or evening to reduce evaporation.",
        "Collect rainwater for outdoor use.",
        "Run full loads in your washing machine and dishwasher.",
        "Use a broom instead of a hose to clean driveways and sidewalks."
    ]

    for tip in tips:
        st.write("- " + tip)

# Function to display water saving calculator
def display_water_saving_calculator():
    st.header("Water Saving Calculator")
    st.write("Calculate potential water savings by implementing water-saving measures.")

    # Add water-saving measures and their estimated savings
    measures = {
        "Low-flow showerhead": 10,  # gallons per day
        "Faucet aerator": 5,  # gallons per day
        "Fixing leaks": 20,  # gallons per day
        # Add more measures as needed
    }

    # Display input fields for selecting measures and their quantity
    selected_measures = st.multiselect("Select water-saving measures:", list(measures.keys()))
    measure_quantities = {measure: st.number_input(f"Quantity for {measure}", min_value=0, max_value=10, value=1) for measure in selected_measures}

    # Calculate total potential water savings
    total_savings = sum(measures[measure] * quantity for measure, quantity in measure_quantities.items())
    st.write(f"Total potential water savings: {total_savings} gallons per day")

# Function to run the Streamlit application
def main():

    # Or display an image from a local file
    image_file = 'C:\\Users\\pugal\\Downloads\\chennaiimage.jpg'
    st.image(image_file, use_column_width=True)

    st.title("Water Management System")

    # Load water consumption data
    df = load_water_data()

    # Sidebar navigation
    menu_selection = st.sidebar.selectbox("Navigation", ["Water Conservation Tips", "Monthly Water Consumption Analytics", "Water Saving Calculator"])

    if menu_selection == "Water Conservation Tips":
        display_water_conservation_tips()
    elif menu_selection == "Monthly Water Consumption Analytics":
        analyze_monthly_water_consumption(df, 'January')  # Change the month as needed
    elif menu_selection == "Water Saving Calculator":
        display_water_saving_calculator()

if __name__ == "__main__":
    main()
