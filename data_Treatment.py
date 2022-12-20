import datetime

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st


class DataTreatment:
    table = pd.read_excel('Data_set/Plan_Out.xlsx', sheet_name=1, usecols=[1,2,3,4,5,6], )

    table = table.dropna(subset=['Unnamed: 3'])