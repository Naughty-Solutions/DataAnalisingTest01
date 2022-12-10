#Importação de Bibliotecas
import pandas as pd
import matplotlib.pyplot as plt

#Importação de Dataset
tabela_sesp = pd.read_excel('C://Users/lucas/Documents/Analise/Data_set/Planilha_Outubro_2022.xlsx', sheet_name=1, usecols=[1,2,3,4,5,6], )

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
#tabela_sesp['DESTINO'].replace(['09:23:00'], 'NÃO DEFINIDO', inplace=True)

#Calculando Dias de Internação
#Adicionando Coluna _DIAS INTERNAÇÃO_
tabela_sesp['DIAS INTERNAÇÃO'] = tabela_sesp['DATA SAÍDA PS'] - tabela_sesp['DATA ENTRADA PS']
#Erro 02
#tabela_sesp['HORA INTERNAÇÃO'] = (tabela_sesp['HORA SAÍDA PS'] - tabela_sesp['HORA ENTRADA PS'])

#Calculando Media de Dias de Internação Geral
media = tabela_sesp['DIAS INTERNAÇÃO'].mean()
print('Média de dias de Internação CD:')
print(media)

#Calculando Media de Dias de Internação Óbito
obito = (tabela_sesp[tabela_sesp['DESTINO']=='ÓBITO'])
print('Média de dias de Internação de PS destino óbito CD:')
media_obito = obito['DIAS INTERNAÇÃO'].mean()
print(media_obito)

#Calculando Media de Dias de Internação Alta
alta = (tabela_sesp[tabela_sesp['DESTINO']=='ALTA'])
media_alta = alta['DIAS INTERNAÇÃO'].mean()
print('Média de dias de Internação de PS destino Alta CD:')
print(media_alta)

#Mostrando Ocorrências de Cada Valor de Destino
tabala_valores = tabela_sesp['DESTINO'].value_counts()

#Mostrando Gráfico de Área de Destino

tabala_valores.plot(kind='area')
plt.show()

#x = ['Média Geral','Média Alta','Média Óbito']
#y = [media, media_alta, media_obito]

#fig, ax = plt.subplots()
#ax.plot(x,y)
#plt.show()