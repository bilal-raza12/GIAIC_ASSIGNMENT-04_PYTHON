import streamlit as st
import pandas as pd


st.set_page_config(
    page_title="BMI Calculator",
    page_icon="🏋️",
    layout="centered",
    initial_sidebar_state="expanded",
)
st.title("BMI Calculator")



weight = st.slider("Enter your weight (in kg)" , 40 , 200 , 70)
height = st.slider("Enter your height (in cm)" , 100 , 250 , 175)
bmi = weight / ((height / 100) ** 2)
st.write(f"Your BMI is: {bmi:.2f}")
st.write("BMI Categories:")
st.write("Underweight: Less than 18.5")
st.write("Normal weight: 18.5–24.9")
st.write("Overweight: 25–29.9")
st.write("Obesity: 30 or greater")




