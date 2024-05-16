import pandas as pd
from datetime import timedelta
from YFinance import YFinance



tabela = pd.read_csv('databreach.csv', sep=',', encoding='ISO-8859-1')

#converte a coluna 'event_date' de Object para tipo date
tabela['event_date'] = pd.to_datetime(tabela['event_date'], format='%d/%m/%Y')

#converte valores null da coluna 'breach_size' em 0
tabela['breach_size'] = tabela['breach_size'].fillna((0))
df = pd.DataFrame(tabela)


date_start = 0
date_end = 0



def converte3 (id):
    date_start = tabela['event_date'][id]-timedelta(3)
    date_end = tabela['event_date'][id]+timedelta(3)
    
    
    df.iat[id,df.columns.get_loc('dif3')] = YFinance.findStocks(tabela['ticker'][id],date_start,date_end)
    df['dif3'] = df['dif3'].astype(float)


def converte7 (id):
    date_start = tabela['event_date'][id]-timedelta(7)
    date_end = tabela['event_date'][id]+timedelta(7)
    
    
    df.iat[id,df.columns.get_loc('dif7')] = YFinance.findStocks(tabela['ticker'][id],date_start,date_end)
    df['dif7'] = df['dif7'].astype(float)

#df_ticker = df.loc[:,'ticker']

#chamada dif3 referente a diferença de 3 dias antes e depois do incidente
#for n, i in df_ticker.items():
#print(n)
converte3(300)
#df = df.rename(columns={'sdr': 'dif3'})
#converte3(299)
#converte7(299)

#df['dif7'][2] = 2.0
print(df.loc[300])
#df.info()
#ind = tabela['ticker']['AMR'].index()
#print(ind)
#print(date_start)



