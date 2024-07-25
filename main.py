import streamlit as st
import plotly.express as px
import functions as fns

st.set_page_config("Weather")

# Front End
st.title("Weather web app")
u_input = st.text_input("Place")
slider = st.slider("Forcast days" , 1 , 5)
box = st.selectbox("Select data to view" 
                   , ["Temperature" , "Sky"])



try:
    # Extraction of data from functions.py
    data = fns.weather_API(u_input,slider)
    # Selection of "Temperature" in selectbox
    if box == "Temperature":
        st.subheader(f"Temperature for the next {slider}\
             days in {u_input}")
        temp = [data[i]["main"]["temp"] -273.15 for i in range(8)]
        date = [dic["dt_txt"] for dic in data]
        graph = px.line(None , date , temp
                        , labels={"x":"Date/Time","y":"Temps"})
        st.plotly_chart(graph)
    # Selection of "Sky" in selectbox
    if box == "Sky":
        sky_cond = [weather["weather"][0]["main"] for weather in data]
        images = {"Clear":"images/clear.png","Clouds":"images/cloud.png"
                      ,"Rain":"images/rain.png","Snow":"images/snow.png"}
        image_gen = [images[condition] for condition in sky_cond]
        st.image(image_gen , width=120)
except:
    st.subheader("No Input")