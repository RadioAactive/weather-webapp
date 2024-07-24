import streamlit as st
import plotly.express as px
import functions as fns

st.set_page_config("Weather")

st.title("Weather web app")
u_input = st.text_input("Place")

slider = st.slider("Forcast days" , 1 , 5)
box = st.selectbox("Select data to view" 
                   , ["Temperature" , "Sky"])



try:    
    data = fns.weather_API(u_input,slider)
    if box == "Temperature":
        st.subheader(f"Temperature for the next {slider}\
             days in {u_input}")
        temp = [data[i]["main"]["temp"] -273.15 for i in range(8)]
        date = [dic["dt_txt"] for dic in data]
        graph = px.line(None , date , temp
                        , labels={"x":"Date/Time","y":"Temps"})
        st.plotly_chart(graph)
except:
    st.subheader("No Input")