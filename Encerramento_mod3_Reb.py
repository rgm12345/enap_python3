import pandas as pd
import streamlit as st
import requests as req

url_F = "https://dadosabertos.camara.leg.br/api/v2/deputados?siglaSexo=F&ordem=ASC&ordenarPor=nome"
url_M = "https://dadosabertos.camara.leg.br/api/v2/deputados?siglaSexo=M&ordem=ASC&ordenarPor=nome"

api_F = req.get(url_F)
api_F = api_F.json()

api_M = req.get(url_M)
api_M = api_M.json()	

df_dep_F = pd.DataFrame(api_F['dados'])
df_dep_F["genero"] = "F"

df_dep_M = pd.DataFrame(api_M['dados'])
df_dep_M["genero"] = "M"

df_dep = pd.concat([df_dep_F, df_dep_M])

st.title("Distribuição de gênero na Câmara dos Deputados")

#total de homens
st.metric('Total de Homens', df_dep_M['id'].count())
#total de mulheres
st.metric('Total de Mulheres', df_dep_F['id'].count())

#item 5
#Filtrando df por sexo
#inserindo um selectbox
filtro_gen = st.selectbox(
    'Qual o gênero cuja distribuição por UF que deseja visualizar?',
     df_dep['genero'].unique())

df_filtrado = df_dep[df_dep['genero'] == filtro_gen]
st.title('Distribuição por UF de Deputados do gênero ' + filtro_gen)


st.bar_chart(df_filtrado,
             x = 'siglaUf',
             y = 'id',
             x_label='Siglas dos estados',
             y_label='Quantidade de deputados')


st.write('A distribuição de gênero para a Câmara dos Deputados é a seguinte:')

fig = px.bar(df_dep,
x='siglaUf', 
y='id', 
color='genero', 
title='Distribuição de gênero na Câmara dos Deputados',
labels={'Quantidade': 'Quantidade', 'UF': 'Unidade Federativa'},
barmode='stack'  #Aqui é onde definimos o stacked bar
)

st.plotly_chart(fig)
