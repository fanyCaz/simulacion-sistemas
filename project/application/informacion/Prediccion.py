import warnings
import itertools
import pandas as pd
import numpy as np
import csv
import statsmodels.api as sm
import matplotlib.pyplot as plt
from pathlib import Path
from pylab import rcParams

import datetime
plt.style.use('fivethirtyeight')

contaminante = 'CA'
#ABRIL
mes = '05'
thisPath = Path(__file__).parent.absolute()
pathAbril = "{}_2020_{}.csv".format(mes,contaminante)
filePathAbril = thisPath/'datos'/pathAbril

dfabril = pd.read_csv( filePathAbril, parse_dates=True, index_col=0)

nivelesAbril = dfabril

nivelesAbril = nivelesAbril.sort_values('fecha')

y = nivelesAbril.mean()

y = y.fillna(y.bfill())

#POR PERIODO DE 12 HORAS, ENTONCES SE HACEN UN 'SEASON' DE UN DÍA A LA MITAD
rcParams['figure.figsize'] = 18,8

decomposition = sm.tsa.seasonal_decompose(y,model='additive',period=4)

#ARIMA
d = p = q = range(0,2)
pdq = list(itertools.product(p,d,q))

seasonal_pdq = [(x[0],x[1],x[2],12) for x in list(itertools.product(p,d,q))]

warnings.filterwarnings("ignore")

for param in pdq:
    for param_seasonal in seasonal_pdq:
        try:
            mod = sm.tsa.statespace.SARIMAX(y,order=param,seasonal_order=param_seasonal,enforce_stationarity=False,enforce_invertibility=False)
            result = mod.fit()
        except:
            continue

mod = sm.tsa.statespace.SARIMAX(y,order=(1,1,1),seasonal_order=(1,1,1,4),enforce_stationarity=False,enforce_invertibility=False)
results = mod.fit()
#Autoregressive Integrated Moving Average.
print(results.summary().tables[1])

#FORECASTING
pred = results.get_prediction(dynamic=False)
pred_ci = pred.conf_int()

#PREDICCIONES
valoresPredecidos = []
minimos = []
for i in pred_ci.iloc[:,0]:
    minimos.append(i)

maximos = []
for i in pred_ci.iloc[:,1]:
    maximos.append(i)

for i in range(0,len(maximos)):
    val = maximos[i] - ( ( maximos[i] - minimos[i] ) / 2 )
    valoresPredecidos.append(val)
print(valoresPredecidos)
mis = pd.DataFrame(valoresPredecidos)
mis.to_csv('promedios_ca.csv',header=False)
#FIN PREDICCIONES

ax = y['0':].plot(label='observados')
pred.predicted_mean.plot(ax=ax, label='prediccion',alpha=.7)
#Datos de prediccion pred_ci
pred_ci.to_csv('prediccion_ca.csv')
ax.fill_between(pred_ci.index, pred_ci.iloc[:,0],pred_ci.iloc[:,1], color='k',alpha=.2)
ax.set_xlabel('Horas')
ax.set_ylabel('Niveles NO2')
plt.legend()

y_forecasted = pred.predicted_mean
y_truth = y['0':]

mse = ((y_forecasted - y_truth) ** 2).mean()
print("Validacion de error : {}".format( round(mse,2) ) )

pred_uc = results.get_forecast(steps=500)
pred_ci = pred_uc.conf_int()
