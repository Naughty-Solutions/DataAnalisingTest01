import datetime

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
from sqlalchemy import create_engine

engine = create_engine('sqlite://', echo=False)

tabela_sesp = pd.read_excel('Data_set/novinho.xlsx',)

tabela_sesp.to_sql('pacientes', con=engine)

engine.execute("SELECT * FROM pacientes").fetchall()