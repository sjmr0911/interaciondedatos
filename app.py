import pandas as pd
import streamlit as st

# Cargar los datos
@st.cache_data
def load_data():
    df = pd.read_csv('Retail_Transaction_Dataset.csv')
    return df

# Función para recomendar productos
def recommend_products(selected_product, df):
    recommendations = df[df['Product'] == selected_product].head(5)
    return recommendations

# Cargar datos
data = load_data()

# Mostrar nombres de las columnas para depuración
st.write("Nombres de las columnas:", data.columns)

# Título de la aplicación
st.title('Sistema de Recomendación de Productos')

# Seleccionar productos
product_list = data['Product'].unique()  # Asegúrate de usar el nombre correcto aquí
selected_product = st.selectbox('Selecciona un producto:', product_list)

# Botón para recomendar productos
if st.button('Recomendar'):
    recommendations = recommend_products(selected_product, data)
    st.write('Productos recomendados:')
    st.dataframe(recommendations)

# Mostrar los datos originales
if st.checkbox('Mostrar datos originales'):
    st.write(data)
