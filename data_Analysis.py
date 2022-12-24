import datetime
import matplotlib.pyplot as plt
import streamlit as st
from io import StringIO 
from data_Treatment import DataTreatment


class DataAnalysis():
    st.markdown(
        "# Analise de Dados de uma Planilha em Excel"
    )
    st.markdown(
        "Analise de dados do Fluxo de Pacientes que percorrem um Pronto Socorro de um Hospital"
    )
    st.markdown(
        "Envie seu arquivo de planilha LOS para analizarmos"
        )
    uploaded_file = st.file_uploader("Insira a tabela do LOS")
    if uploaded_file is not None:
        table = DataTreatment.read_excel_LOS(uploaded_file) 
        name_PS = 'NAME PS'
        entry_date = 'ENTRY DATE PS'
        entry_hour = 'ENTRY HOUR PS'
        exit_date = 'EXIT DATE PS'
        exit_hour = 'EXIT HOUR PS'
        destination = 'DESTINATION'
        datetimeExit = 'DATETIME EXIT PS'
        datetimeEntry = 'DATETIME ENTRY PS'
        datetimeDelta = 'DATETIME DELTA PS'

        # table = DataTreatment.read_excel_LOS('Data_set/Plan_Nov.xlsx')
        DataTreatment.rename_columns_LOS(table)
        DataTreatment.treatment_of_the_wrong_names_of_destination(table[destination])
        DataTreatment.eliminating_errors_date_collums(table[entry_date])
        DataTreatment.eliminating_errors_date_collums(table[entry_hour])
        DataTreatment.eliminating_errors_date_collums(table[exit_date])
        DataTreatment.eliminating_errors_date_collums(table[exit_hour])
        DataTreatment.check_values_destination(table[destination])

        def combineDateTime(listDate, listTime):
            dateList = []
            for date,time in zip(listDate,listTime):       
                DateTime = datetime.datetime(date.year, date.month, date.day,time.hour, time.minute)
                dateList.append(DateTime)
            return dateList 

        table[datetimeExit] = combineDateTime(table[exit_date],table[exit_hour])
        table[datetimeEntry] = combineDateTime(table[entry_date],table[entry_hour])

        def CalculationDateTimeDelta(listEntrada,listSaida):
            dateList = []
            for entrada,saida in zip(listEntrada,listSaida):
                delta = saida-entrada
                dateList.append(delta)
            return dateList

        table[datetimeDelta] = CalculationDateTimeDelta(table[datetimeEntry],table[datetimeExit])

        meanDelta = table[datetimeDelta].mean()
        print(f"Mean time of the PS: {meanDelta}")

        obito = (table[table[destination] == 'ÓBITO'])
        obito_mean = obito[datetimeDelta].mean()
        print(f"Mean of the days in the PS with destination death: {obito_mean}")

        release = (table[table[destination] == 'ALTA'])
        release_mean = release[datetimeDelta].mean()
        print(f"Mean of the days in the PS with destination release: {release_mean}")

        evasion = (table[table[destination] == 'EVASÃO'])
        evasion_mean = evasion[datetimeDelta].mean()
        print(f"Mean of the days in the PS with destination evasion: {evasion_mean}")

        table_values = table[destination].value_counts()
        table_values_entry = table[entry_date].value_counts()

        #Mostrando Gráfico de Área de Destino
        dataChart = table_values.plot(kind='area')
        
        st.markdown(
            "## Grafico de Area exibindo a quantidade de Altas em relação as Evasões e Altas"
        )
        st.area_chart(table_values)

        st.markdown(
            "## Grafico de Area exibindo os dias com mais atendimentos"
        )
        st.area_chart(table_values_entry)

        #Grafico de Pizza
        st.markdown(
            "## Porcentagens"
        )

        labels = 'Altas', 'Evasão', 'Obito'
        sizes = [release[destination].count(), evasion[destination].count(),obito[destination].count()]
        colors = ['#2E9AFF', '#b80606','white']
        explode = [0.2,0,0]
        fig1, ax1 = plt.subplots()

        #ax1.barh(labels,sizes)
        #plt.show()
        #Setando Atributos no Grafico de Pizza
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
            f"### :heart: Altas: {release[destination].count()} | :runner: Evasões: {evasion[destination].count()} |   :skull: Obitos: {obito[destination].count()} | :hospital: Total de Pacientes: {table[destination].count()}"
        )

        probabilidade_Evasao = (evasion[destination].count() / table[destination].count())*100
        st.markdown(
            f"### Probabilidade de ocorrer uma Evasão no PS: {probabilidade_Evasao:.1f}% "
        )
        

