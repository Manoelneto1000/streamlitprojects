import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv("Frutas.csv", sep=';', encoding='latin1')

DadosGrafico = pd.DataFrame(
    np.random.randn(20,3), 
    columns=["amor","buser", "casa"]
)

st.write("Hello word")
x = st.text_input("Qual o seu filme favorito?")
st.write(f"O seu filme favorito é {x}")
st.button("Clique aqui")
st.write("## Isso é um texo em tag h2")
st.write("### Isso é um texo em tag h3")
st.write("Pode consultar em https://docs.streamlit.io/develop/api-reference/text/st.markdown")

st.write(df)

st.write("## Gráfico de linha")
st.line_chart(DadosGrafico)
