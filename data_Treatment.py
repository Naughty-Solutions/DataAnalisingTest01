import datetime

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st


class DataTreatment:
    def read_excel_LOS(path):  
        table = pd.read_excel(path, sheet_name=1, usecols=[1,2,3,4,5,6],skiprows=range(0,4)  )
        return table
    def rename_columns_LOS(table):
        table.dropna(subset=['HORA ENTRADA PS'], inplace= True)
        #Rename Collums
        table.rename(columns={'NOME PACIENTE (OPCIONAL)': 'NAME PS'},inplace= True)
        table.rename(columns={'DATA ENTRADA PS': 'ENTRY DATE PS'},inplace= True)
        table.rename(columns={'HORA ENTRADA PS': 'ENTRY HOUR PS'},inplace= True)
        table.rename(columns={'DATA SAÍDA PS': 'EXIT DATE PS'},inplace= True)
        table.rename(columns={'HORA SAÍDA PS': 'EXIT HOUR PS'},inplace= True)
        table.rename(columns={'DESTINO': 'DESTINATION'},inplace= True)
        table.reset_index(drop=True,inplace=True)
    # def treatment_of_the_nulls(table):
    #     #table = table.loc[4:]
    #     table.reset_index(drop=True,inplace=True)
    def treatment_of_the_wrong_names_of_destination(SerieDestination):
        SerieDestination.replace('OBITO', 'ÓBITO', inplace=True)
        SerieDestination.replace('EVASAO', 'EVASÃO', inplace=True)
        SerieDestination.replace('EVSÃO', 'EVASÃO', inplace=True)

    def treatment_all(table):
        #Defining variables for fa
        name_PS = 'NAME PS'
        entry_date = 'ENTRY DATE PS'
        entry_hour = 'ENTRY HOUR PS'
        exit_date = 'EXIT DATE PS'
        exit_hour = 'EXIT HOUR PS'
        destination = 'DESTINATION'






    def eliminating_errors_date_collums(seriesList):
        count = 0
        for value in seriesList:
            if type(value) == str:
                print(f"The value of error in the Colunm DateTime: {value} Index: {count}")
                print(f"Confirmation of the error index: {seriesList[count]}")
                seriesList.replace(seriesList[count],seriesList[(count-1)],inplace = True)
                print(f"The value after the treatment: {seriesList[count]}")
            count += 1
            
    def check_values_destination(seriesDestination):
        count = 0
        for value in seriesDestination:
            if type(value) != str:
                print(f"The value of error in the Colunm Destination: {value} Index: {count}")
                print(f"Confirmation of the error index: {seriesDestination[count]}")
                seriesDestination.replace(seriesDestination[count],seriesDestination[count+1], inplace= True)
                print(f"The value after the treatment: {seriesDestination[count]}")
            count += 1
        