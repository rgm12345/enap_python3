import streamlit as st

st.write("Este é meu primeiro Deploy")


st.title("Este é o título do app")
st.header("Este é o subtítulo")
st.subheader("Este é o terceiro subtítulo")
st.markdown("Este é texto")
st.caption("Esta é a a legenda")
st.code("x=2021")
st.latex(r''' a+a r^1+a r^2+a r^3 ''')

grau_satisfacao = st.select_slider(
    'Qual o seu grau de satisfação?',
    options=range(0, 101))

st.write('O cliente respondeu:', grau_satisfacao)
