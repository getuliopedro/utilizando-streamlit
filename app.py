import streamlit as st 
import pandas as pd

st.set_page_config("Meu site Streamlit")

with st.container():
    st.subheader("Meu primeiro site usando streamlit")
    st.title("Dashboard de Contratos")
    st.write("Informacoes de contratos fechado pela HeitEven Tech ao longo de Maio")
    st.write("Visite meu repositorio! [Clique aqui](https://github.com/getuliopedro?tab=repositories)")
    
    
@st.cache_data    
def carregar_dados():
    
    tabela = pd.read_csv("resultados.csv")
    return tabela
    
with st.container():
    st.write("---")
    quant_dias = st.selectbox("Selecione  periodo",["7D", "15D", "21D", "30D"])
    num_dias = int(quant_dias.replace("D",""))
    dados = carregar_dados()
    dados =dados[-num_dias:]
    
    st.area_chart(dados, x="Data", y="Contratos")