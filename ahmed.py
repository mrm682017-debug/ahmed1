# a=float("enter height")

# b=float("enter weight")

# result=a/b

# import streamlit as st

# st.set_page_config(page_title="BMI Calculator", page_icon="⚖️")

# st.title("⚖️ BMI Calculator")
# st.write("Enter your details below to calculate your Body Mass Index.")

# # Create two columns for a cleaner layout
# col1, col2 = st.columns(2)

# with col1:
#     weight = st.number_input("Weight (kg)", min_value=1.0, value=70.0, step=0.1)

# with col2:
#     # Assuming height in meters for the standard formula
#     height = st.number_input("Height (m)", min_value=0.5, value=1.70, step=0.01)

# if st.button("Calculate BMI"):
#     # Calculate BMI: weight / height squared
#     bmi = weight / (height ** 2)
    
#     st.divider()
#     st.subheader(f"Your BMI is: {bmi:.2f}")
    
#     # Logic for BMI Categories
#     if bmi < 18.5:
#         st.warning("Category: Underweight")
#     elif 18.5 <= bmi < 25:
#         st.success("Category: Normal weight")
#     elif 25 <= bmi < 30:
#         st.info("Category: Overweight")
#     else:
#         st.error("Category: Obesity")

# st.info("Note: BMI is a general indicator and does not account for muscle mass or body composition.")
import streamlit as st
import matplotlib.pyplot as plt

# Page config
st.set_page_config(
    page_title="BMI Calculator Pro",
    page_icon="⚖️",
    layout="centered"
)

# Sidebar
st.sidebar.title("⚙️ Settings")
dark_mode = st.sidebar.toggle("🌙 Dark Mode")
show_chart = st.sidebar.checkbox("📈 Show BMI Chart", value=True)

# Dark / Light CSS
if dark_mode:
    bg_color = "#0e1117"
    card_color = "#161b22"
    text_color = "white"
else:
    bg_color = "#f5f7fb"
    card_color = "white"
    text_color = "black"

# Custom CSS
st.markdown(f"""
<style>
.main {{
    background-color: {bg_color};
    color: {text_color};
}}
.bmi-card {{
    background: {card_color};
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.2);
    text-align: center;
}}
</style>
""", unsafe_allow_html=True)

# Title
st.title("⚖️ BMI Calculator Pro")
st.write("Calculate your **Body Mass Index** with smart insights 💡")

# Input layout
col1, col2 = st.columns(2)

with col1:
    weight = st.number_input("⚖️ Weight (kg)", 1.0, 300.0, 70.0, 0.1)

with col2:
    height = st.number_input("📏 Height (m)", 0.5, 2.5, 1.70, 0.01)

# Calculate button
if st.button("🚀 Calculate BMI"):
    bmi = weight / (height ** 2)

    st.markdown('<div class="bmi-card">', unsafe_allow_html=True)
    st.subheader(f"📊 Your BMI: **{bmi:.2f}**")

    # BMI logic + tips
    if bmi < 18.5:
        st.warning("🟡 Underweight")
        st.progress(25)
        tip = "🍎 Eat nutrient-dense foods & consult a nutritionist."
    elif 18.5 <= bmi < 25:
        st.success("🟢 Normal weight")
        st.progress(50)
        tip = "💪 Great job! Maintain diet & regular exercise."
    elif 25 <= bmi < 30:
        st.info("🟠 Overweight")
        st.progress(75)
        tip = "🏃‍♂️ Add cardio & reduce sugary foods."
    else:
        st.error("🔴 Obesity")
        st.progress(100)
        tip = "🧑‍⚕️ Consult a doctor & follow a structured plan."

    st.markdown(f"### 🧑‍⚕️ Health Tip\n{tip}")
    st.markdown('</div>', unsafe_allow_html=True)

    # BMI Chart
    if show_chart:
        st.subheader("📈 BMI Range Chart")

        categories = ["Underweight", "Normal", "Overweight", "Obese"]
        values = [18.5, 24.9, 29.9, bmi]

        fig, ax = plt.subplots()
        ax.bar(categories, values, color=["gold", "green", "orange", "red"])
        ax.set_ylabel("BMI Value")
        ax.set_title("BMI Comparison")

        st.pyplot(fig)

# Footer
st.divider()
st.caption("📱 Mobile-friendly • 🌈 Dark mode • 📊 Smart insights")
st.info("ℹ️ BMI is an indicator only. It does not measure body fat or muscle mass.")
