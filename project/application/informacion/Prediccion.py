import warnings
import itertools
import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
from pathlib import Path
from pylab import rcParams

import datetime
plt.style.use('fivethirtyeight')

#MAYO
mes= '05'
contaminante = 'SO2'
path = "{}_2020_{}.csv".format(mes,contaminante)
thisPath = Path(__file__).parent.absolute()
filePath = thisPath/'datos'/path
df = pd.read_csv(filePath)
#ABRIL
mes = '05'
pathAbril = "{}_2020_{}.csv".format(mes,contaminante)
filePathAbril = thisPath/'datos'/pathAbril
#f = lambda s: datetime.datetime.strptime(s,'%Y-%m-%d')
dfabril = pd.read_csv( filePathAbril, parse_dates=True, index_col=0)
print(dfabril)
print(dfabril.index)

""" nivelesMayo = df.loc[0:,'0':'23']
nivelesAbril = dfabril

print( "niveles abril" )
#print( nivelesAbril['fecha'].min() )

nivelesAbril = nivelesAbril.sort_values('fecha')

#print( nivelesAbril.isnull().sum() )

nivelesAbril = nivelesAbril.groupby('fecha').sum().reset_index()

nivelesAbril = nivelesAbril.set_index('fecha')

print(nivelesAbril.index)
#print(nivelesAbril)

y = nivelesAbril.mean()
print(y)
y.plot(figsize=(15,6))
#plt.show()

rcParams['figure.figsize'] = 18,8

decomposition = sm.tsa.seasonal_decompose(y,model='additive')
fig = decomposition.plot()
plt.show()
 promedios = []
print(len(nivelesMayo) - 1)
for j in range(0,len(nivelesMayo)):     #promedio de contaminante por dia
    promedios.append( nivelesMayo.iloc[j].mean() )
    
for j in range(0,len(nivelesAbril)):
    promedios.append( nivelesAbril.iloc[j].mean() )

pror = np.array(promedios)
print(pror)
fig,ax = plt.subplots()
ax.plot( np.arange(0,31), pror )
plt.show()

print("index : {}" .format(nivelesMayo.index) ) """