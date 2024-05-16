import pandas as pd
from datetime import timedelta
from YFinance import YFinance



tabela = pd.read_csv('databreach.csv', sep=',', encoding='ISO-8859-1')

#converte a coluna 'event_date' de Object para tipo date
tabela['event_date'] = pd.to_datetime(tabela['event_date'], format='%Y-%m-%d')

#converte valores null da coluna 'breach_size' em 0
tabela['breach_size'] = tabela['breach_size'].fillna((0))



date_start = 0
date_end = 0


#Pega o ticker no dataset databreach.csv e busca via API na plataforma YFinance fazendo o SDT de trÊs dias antes e depois da divulgação dos ataques.
def converte3 (id):
    date_start = tabela['event_date'][id]-timedelta(3)
    date_end = tabela['event_date'][id]+timedelta(3)
    tabela.loc[id, 'dif3'] = YFinance.findStocks(tabela['ticker'][id],date_start,date_end)
    tabela['dif3'] = tabela['dif3'].astype(float)

#Pega o ticker no dataset databreach.csv e busca via API na plataforma YFinance fazendo o SDT de sete dias antes e depois da divulgação dos ataques.
def converte7 (id):
    date_start = tabela['event_date'][id]-timedelta(7)
    date_end = tabela['event_date'][id]+timedelta(7)
    tabela.loc[id, 'dif7'] = YFinance.findStocks(tabela['ticker'][id],date_start,date_end)
    tabela['dif7'] = tabela['dif7'].astype(float)

for n in range(len(tabela)):
 
    print(n)

    converte7(n)
    print(tabela.loc[n])
    tabela.to_csv('databreach.csv', index=False)
