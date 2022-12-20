import datetime

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
import sqlite3

conn = sqlite3.connect('test_database')
c = conn.cursor()

c.execute(
    'CREATE TABLE IF NOT EXISTS patients (NAME_PS text, ENTRY_DATE_PS,ENTRY_HOUR_PS,EXIT_DATE_PS,EXIT_HOUR_PS,DESTINATION)')
conn.commit()


class DataTreatment:
    table = pd.read_excel('Data_set/Plan_Out.xlsx', sheet_name=1, usecols=[1,2,3,4,5,6], )

    table = table.dropna(subset=['Unnamed: 3'])

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

    table.to_sql('patients', conn, if_exists='replace', index = False)

    c.execute('''  
    SELECT * FROM patients
          ''')

    for row in c.fetchall():
        print (row)

    def check_values_destination(seriesDestination):
        for value in seriesDestination:
            if value != 'OBITO' and value != 'EVASÃO' and value != 'EVASAO' and value != 'ALTA':
                print(f"Valor escrito errado: {value}")
                print(f"Tipo dele: {type(value)}")
            if type(value) != str:
                print(f"Tem um numero aqui: {value}")
        
    #check_values_destination(table[destination])