import streamlit as st
import plotly.express as px

st.set_page_config("Weather")

st.title("Weather web app")
u_input = st.text_input("Place")

slider = st.slider("Forcast days" , 1 , 5)
box = st.selectbox("Select data to view" 
                   , ["Temperature" , "Sky"])

st.subheader(f"Temperature for the next {slider}\
             days in {u_input}")