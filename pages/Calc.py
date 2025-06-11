import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import math

st.title("Calculadora")

st.write("### Insira os dados")
col1, col2, col3 = st.columns(3)
with col1:
    home_value=col1.number_input("Valor inicial", min_value=0, value=500000)
    deposit = col1.number_input("Deposit", min_value=0, value=100000)
    st.text("Ola")
with col2:
    interest_rate=col2.number_input("Rate", min_value=0.0, value=5.5)
    loan_term=col2.number_input("Loan", min_value=1, value=30)
    st.text("Ola 2") 

with col3:
    st.text("1")
    st.text("1")
    st.text("1")
    st.text("1")
    loan_termq=col3.number_input("Loanqqq", min_value=1, value=30)
    