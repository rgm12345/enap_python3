import streamlit as st

st.write("Este é meu primeiro Deploy")


st.title("Este é o 1o aplicativo da Rebeca")
#st.header("Este é o subtítulo")
#st.subheader("Este é o terceiro subtítulo")
st.markdown("Vamos fazer uma tentativa...")
#st.caption("Esta é a a legenda")
#st.code("x=2021")
#st.latex(r''' a+a r^1+a r^2+a r^3 ''')

'''grau_satisfacao = st.select_slider(
    'Qual o seu grau de satisfação?',
    options=range(0, 101))

st.write('O cliente respondeu:', grau_satisfacao)'''

st.button('Clique')
st.radio('Selecione seu gênero',['Masculino','Feminino'])
st.multiselect('Escolha um departamento',['SOF', 'ENAP', 'UFs'])
st.select_slider('Selecione uma resposta', ['Ruim', 'Bom', 'Excelente'])
st.slider('Selecione um número', 0,50)
st.number_input('Selecione um número', 0,10)
st.text_input('Endereço de e-mail')
st.date_input('Data de viagem')
st.time_input('Tempo de escola')
st.text_area('Descrição')
st.file_uploader('Atualize uma foto')
st.color_picker('Escolha sua cor favorita')




