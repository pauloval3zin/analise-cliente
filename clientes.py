import pandas as pd

tabela = pd.read_csv("clientes.csv", encoding='Latin1', sep=';') 
print(tabela.info())
tabela = tabela.drop("Unnamed: 8", axis=1)

tabela['Salário Anual (R$)'] = pd.to_numeric(tabela['Salário Anual (R$)'], errors='coerce') 

tabela = tabela.dropna() 
print(tabela.info()) 

print(tabela.describe()) 

import plotly.express as px 
for coluna in tabela.columns: 
    grafico = px.histogram(tabela, x=coluna, y="Nota (1-100)", histfunc="avg", text_auto=True)
    grafico.show() 
