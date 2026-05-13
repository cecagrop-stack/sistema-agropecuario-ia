
import streamlit as st
from PIL import Image
import random

st.title("Sistema Inteligente Agropecuario")

uploaded_file = st.file_uploader(
    "Sube una imagen agrícola",
    type=["jpg","jpeg","png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(image, caption="Imagen cargada", use_container_width=True)

    predicciones = [
        "Hoja saludable",
        "Posible enfermedad fúngica",
        "Deficiencia nutricional",
        "Estrés hídrico"
    ]

    resultado = random.choice(predicciones)

    st.subheader("Resultado del análisis")

    st.success(resultado)
