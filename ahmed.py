import streamlit as st

st.set_page_config(page_title="BMI Calculator", page_icon="⚖️")

st.title("⚖️ BMI Calculator")
st.write("Enter your details below to calculate your Body Mass Index.")

# Create two columns for a cleaner layout
col1, col2 = st.columns(2)

with col1:
    weight = st.number_input("Weight (kg)", min_value=1.0, value=70.0, step=0.1)

with col2:
    # Assuming height in meters for the standard formula
    height = st.number_input("Height (m)", min_value=0.5, value=1.70, step=0.01)

if st.button("Calculate BMI"):
    # Calculate BMI: weight / height squared
    bmi = weight / (height ** 2)
    
    st.divider()
    st.subheader(f"Your BMI is: {bmi:.2f}")
    
    # Logic for BMI Categories
    if bmi < 18.5:
        st.warning("Category: Underweight")
    elif 18.5 <= bmi < 25:
        st.success("Category: Normal weight")
    elif 25 <= bmi < 30:
        st.info("Category: Overweight")
    else:
        st.error("Category: Obesity")

st.info("Note: BMI is a general indicator and does not account for muscle mass or body composition.")