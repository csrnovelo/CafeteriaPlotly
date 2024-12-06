import streamlit as st
import pandas as pd
import calendar
import plotly.express as px

pd.options.plotting.backend = "plotly"

st.header("Datos cafetaria")

dfCafeteria = pd.read_csv("Datos/CafeDatosFinalesNov2024.csv")

dfCafeteria.drop(columns=["Unnamed: 0", "index", "temp"], inplace=True)

nombreDias = list(calendar.day_name)

st.dataframe(dfCafeteria)
# valoresDias = dfCafeteria["diaDeLaSemana"].unique()
with st.sidebar:
    diasSemana = st.selectbox(
        "Elige un dia de la semana",
        (nombreDias)
    )

st.write("Día elegido:", diasSemana)

tituloFiltro = "Seleccionando solamente el día:", diasSemana
st.header(tituloFiltro)

dfFiltrado = dfCafeteria[ dfCafeteria["diaDeLaSemana"] == diasSemana]

st.dataframe(dfFiltrado)

contadores = dfCafeteria["diaDeLaSemana"].value_counts()
dfContadores = contadores.rename_axis('Día de la semana').reset_index(name='contador')

fig = px.bar(dfContadores, x='Día de la semana', y='contador', title='Número de visitas por día')

st.plotly_chart(fig,use_container_width=True)