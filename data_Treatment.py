import datetime

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st


class DataTreatment:
    table = pd.read_excel('Data_set/Plan_Out.xlsx', sheet_name=1, usecols=[1,2,3,4,5,6], )

    table = table.dropna(subset=['Unnamed: 3'])

    #Rename Collums
    table = table.rename(columns={'Unnamed: 1': 'NAME PS'})
    table = table.rename(columns={'Unnamed: 2': 'ENTRY DATE PS'})
    table = table.rename(columns={'Unnamed: 3': 'ENTRY HOUR PS'})
    table = table.rename(columns={'Unnamed: 4': 'EXIT DATE PS'},)
    table = table.rename(columns={'Unnamed: 5': 'EXIT HOUR PS'},)
    table = table.rename(columns={'Unnamed: 6': 'DESTINATION'})

    #Defining variables for fa
    name_PS = 'NAME PS'
    entry_date = 'ENTRY DATE PS'
    entry_hour = 'ENTRY HOUR PS'
    exit_date = 'EXIT DATE PS'
    exit_hour = 'EXIT HOUR PS'
    destination = 'DESTINATION'

    table = table.loc[4:]



    table[destination].replace('OBITO', 'ÓBITO', inplace=True)
    table[destination].replace('EVASAO', 'EVASÃO', inplace=True)
    table[destination].replace('EVSÃO', 'EVASÃO', inplace=True)

    def check_values_destination(Dataframe,seriesDestination):
        count = 1
        for value in seriesDestination:
            if type(value) != str:
                print(f"Tem um numero aqui: {value} Linha: {count}")
                print(f"Confirmando o index do erro: {seriesDestination[count]}")
                #seriesDestination.replace(seriesDestination[count],seriesDestination[count+1])
                print(f"Agora ele ta assim: {seriesDestination[count]}")
            count += 1
        count = 4
        return Dataframe
        
    table = check_values_destination(table,table[destination])
    print