import streamlit as st
import pandas as pd

st.title("Análisis de Transacciones Minoristas")

# Cargar el conjunto de datos
@st.cache
def load_data():
    df = pd.read_csv('Retail_Transaction_Dataset.csv')
    return df

# Cargar datos
data = load_data()

# Mostrar datos
if st.checkbox("Mostrar datos del conjunto"):
    st.write(data)

# Selección de columnas para análisis
st.sidebar.header("Opciones de Análisis")
columnas = data.columns.tolist()
opcion_columna = st.sidebar.selectbox("Selecciona una columna para visualizar:", columnas)

# Mostrar estadísticas descriptivas de la columna seleccionada
if st.sidebar.button("Mostrar estadísticas"):
    st.write(data[opcion_columna].describe())

# Gráficos simples
st.sidebar.header("Gráficos")
grafico_opcion = st.sidebar.selectbox("Selecciona un tipo de gráfico:", ["Histograma", "Gráfico de dispersión"])

if grafico_opcion == "Histograma":
    st.subheader(f"Histograma de {opcion_columna}")
    st.bar_chart(data[opcion_columna].value_counts())
elif grafico_opcion == "Gráfico de dispersión":
    col_x = st.sidebar.selectbox("Selecciona la columna X:", columnas)
    col_y = st.sidebar.selectbox("Selecciona la columna Y:", columnas)
    st.subheader(f"Gráfico de dispersión: {col_x} vs {col_y}")
    st.scatter_chart(data[[col_x, col_y]])
