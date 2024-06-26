import pandas as pd
import plotly.express as px
import streamlit as st
st.header('Análisis Exploratorio de Datos de Vehículos')

car_data = pd.read_csv('vehicles_us.csv')

hist_button = st.button('Construir histograma')

if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:
    st.write('Creación de un gráfico de dispersión')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)

build_histogram = st.checkbox('Construir un histograma')
build_scatter = st.checkbox('Construir gráfico de dispersión')

if build_histogram:
    st.write('Construir un histograma para la columna odómetro')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

if build_scatter:
    st.write('Construir un gráfico de dispersión')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)

car_data = pd.read_csv('vehicles_us.csv') # leer los datos

        
if hist_button: # al hacer clic en el botón
            # escribir un mensaje
            st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
            fig = px.histogram(car_data, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
            st.plotly_chart(fig, use_container_width=True)
