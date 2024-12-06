import streamlit as st
import calendar
from bs4 import BeautifulSoup
import requests
import pandas as pd
import urllib.parse
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sb

# pd.options.plotting.backend = "plotly"
#
# st.header("Datos ventas")
#
# dfVenta = pd.read_csv("Datos/DetalleVenta.csv")
#
# st.dataframe(dfVenta)

url = "https://www.mercadolibre.com.mx/ofertas#nav-header"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
articulos = soup.find_all('div', class_='andes-card poly-card poly-card--grid-card andes-card--flat andes-card--padding-0 andes-card--animated')

data = []

# Iterar sobre los artículos y extraer la información
for articulo in articulos:
    titulo = articulo.find('a', class_='poly-component__title').text.strip() if articulo.find('a', class_='poly-component__title') else None
    url_articulo = articulo.find('a', class_='poly-component__title')['href'] if articulo.find('a', class_='poly-component__title') else None
    precio_anterior = articulo.find('s', class_='andes-money-amount--previous').text.strip() if articulo.find('s', class_='andes-money-amount--previous') else None
    precio_actual = articulo.find('span', class_='andes-money-amount--cents-superscript').text.strip() if articulo.find('span', class_='andes-money-amount--cents-superscript') else None
    descuento = articulo.find('span', class_='andes-money-amount__discount').text.strip() if articulo.find('span', class_='andes-money-amount__discount') else None
    envio = articulo.find('div', class_='poly-component__shipping').text.strip() if articulo.find('div', class_='poly-component__shipping') else None
    imagen = articulo.find('img', class_='poly-component__picture')['data-src'] if articulo.find('img', class_='poly-component__picture') else None

    # Agregar los datos al listado
    data.append({
        'titulo': titulo,
        'url': url_articulo,
        'precio_anterior': precio_anterior,
        'precio_actual': precio_actual,
        'descuento': descuento,
        'envio': envio,
        'imagen': imagen
    })

# Convertir la lista de datos a un DataFrame de pandas
dfArticulos = pd.DataFrame(data)

st.header("Articulos de Mercado Libre")
st.dataframe(dfArticulos)

