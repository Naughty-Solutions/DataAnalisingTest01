#Importação de Bibliotecas
import datetime

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

#Importação de Dataset
tabela_sesp = pd.read_excel('Data_set/plan_Out.xlsx', sheet_name=1, usecols=[1,2,3,4,5,6], )

#Tratamento de Dados
#Remoção de Informações Nulas
tabela_sesp = tabela_sesp.dropna(subset=['Unnamed: 3'])

#Tratamento de Dados
#Troca Renomeando Colunas
tabela_sesp = tabela_sesp.rename(columns={'Unnamed: 1': 'NOME PS'})
tabela_sesp = tabela_sesp.rename(columns={'Unnamed: 2': 'DATA ENTRADA PS'})
tabela_sesp = tabela_sesp.rename(columns={'Unnamed: 3': 'HORA ENTRADA PS'})
tabela_sesp = tabela_sesp.rename(columns={'Unnamed: 4': 'DATA SAÍDA PS'})
tabela_sesp = tabela_sesp.rename(columns={'Unnamed: 5': 'HORA SAÍDA PS'})
tabela_sesp = tabela_sesp.rename(columns={'Unnamed: 6': 'DESTINO'})

#Ocultando Linhas inicias
tabela_sesp = tabela_sesp.loc[4:]

#Tratamento de Dados
#Renomeando Dados
tabela_sesp['DESTINO'].replace('OBITO', 'ÓBITO', inplace=True)
tabela_sesp['DESTINO'].replace('EVASAO', 'EVASÃO', inplace=True)
tabela_sesp['DESTINO'].replace('EVSÃO', 'EVASÃO', inplace=True)

#Erro 01
hourError = datetime.time(hour=9, minute=23)
tabela_sesp['DESTINO'].replace(hourError, 'NÃO DEFINIDO', inplace=True)


#Calculando Dias de Internação
#Adicionando Coluna _DIAS INTERNAÇÃO_
tabela_sesp['DIAS INTERNAÇÃO'] = tabela_sesp['DATA SAÍDA PS'] - tabela_sesp['DATA ENTRADA PS']
#Erro 02

#Converter Horas em Horas com Dia:
#Criando as listas auxiliares
listSaida = []
listEntrada = []
listDelta = []
#Instanciando as colunas com outras para ficar tudo do mesmo tamanho(Tava dando erro sem isso)
tabela_sesp['DATETIME SAÍDA PS'] = tabela_sesp['HORA SAÍDA PS']
tabela_sesp['DATETIME ENTRADA PS'] = tabela_sesp['HORA ENTRADA PS']
tabela_sesp['DATETIME DELTA'] = tabela_sesp['HORA ENTRADA PS'] #Chamei de Delta porque é o nome do tipo que retorna a subtração de datas

#Criando uma Coluna com a Data e Hora de Saida

#Função que combina uma coluna de Date com uma coluna de Time, fazendo uma coluna DateTime
def combineDateTime(listDate, listTime,listDateTime):
    for date,time in zip(listDate,listTime):
        DateTime = DateTime = datetime.datetime(date.year, date.month, date.day,time.hour, time.minute)
        listDateTime.append(DateTime)
    return listDateTime

#Criando as Colunas DateTime para fazer os calculos do tempo medio
tabela_sesp['DATETIME SAÍDA PS'] = combineDateTime(tabela_sesp['DATA SAÍDA PS'],tabela_sesp['HORA SAÍDA PS'],listSaida)
tabela_sesp['DATETIME ENTRADA PS'] = combineDateTime(tabela_sesp['DATA ENTRADA PS'],tabela_sesp['HORA ENTRADA PS'],listEntrada)

#Função que faz a Subtração das datas para saber o tempo medio total
def CalculationDateTimeDelta(listEntrada,listSaida,listDelta):
    for entrada,saida in zip(listEntrada,listSaida):
        delta = saida-entrada
        listDelta.append(delta)
    return listDelta

#Adicionando os valores da lista na Coluna DATETIME DELTA
tabela_sesp['DATETIME DELTA'] = CalculationDateTimeDelta(tabela_sesp['DATETIME ENTRADA PS'],tabela_sesp['DATETIME SAÍDA PS'], listDelta) 

#Calculando Media de Tempo Total:
mediaDelta = tabela_sesp['DATETIME DELTA'].mean()
print(f"Media do tempo Total de Internação: {mediaDelta}")

#Calculando Media de Dias de Internação Geral
media = tabela_sesp['DIAS INTERNAÇÃO'].mean()
print(f'Média de dias de Internação CD: {media}')

#Calculando Media de Dias de Internação Óbito
obito = (tabela_sesp[tabela_sesp['DESTINO']=='ÓBITO'])
media_obito = obito['DATETIME DELTA'].mean()
print(f'Média de dias de Internação de PS destino óbito CD: {media_obito}')


#Calculando Media de Dias de Internação Alta
alta = (tabela_sesp[tabela_sesp['DESTINO']=='ALTA'])
media_alta = alta['DATETIME DELTA'].mean()
print(f'Média de dias de Internação de PS destino Alta CD: {media_alta}')

#Calculando Media de Dias de Internação Evasão
evasao = (tabela_sesp[tabela_sesp['DESTINO']=='EVASÃO'])
media_evasao = evasao['DATETIME DELTA'].mean()
print(f'Média de dias de Internação de PS destino Evasão CD: {media_evasao}')

#Mostrando Ocorrências de Cada Valor de Destino
tabala_valores = tabela_sesp['DESTINO'].value_counts()

st.markdown(
    "# Analise de Dados de uma Planilha em Excel"
)
st.markdown(
    "Analise de dados do Fluxo de Pacientes que percorrem um Pronto Socorro de um Hospital"
)
#Mostrando Gráfico de Área de Destino
dataChart = tabala_valores.plot(kind='area')
st.markdown(
    "## Grafico de Area"
)
st.area_chart(tabala_valores)

#Grafico de Torta
st.markdown(
    "## Porcentagens"
)
labels = 'Altas', 'Evasão', 'Obito'
sizes = [alta['DESTINO'].count(), evasao['DESTINO'].count(),obito['DESTINO'].count()]
colors = ['#2E9AFF', '#b80606','white']
explode = [0.2,0,0]
fig1, ax1 = plt.subplots()
ax1.pie(sizes,
labels = labels, 
autopct='%1.1f%%',
textprops={'color':"#fafafa", 'font':'sans serif'},
colors=colors, 
explode=explode,
shadow= True
)
fig1.set_facecolor("#0e1117")
st.pyplot(fig1)
st.markdown(
    f"### :heart: Altas: {alta['DESTINO'].count()} | :runner: Evasões: {evasao['DESTINO'].count()} |   :skull: Obitos: {obito['DESTINO'].count()} | :hospital: Total de Pacientes: {tabela_sesp['DESTINO'].count()}"
)

probabilidade_Evasao = (evasao['DESTINO'].count() / tabela_sesp['DESTINO'].count())*100
st.markdown(
    f"### Probabilidade de ocorrer uma Evasão no PS: {probabilidade_Evasao:.1f}% "
)



#x = ['Média Geral','Média Alta','Média Óbito']
#y = [media, media_alta, media_obito]

#fig, ax = plt.subplots()
#x.plot(x,y)
#plt.show()