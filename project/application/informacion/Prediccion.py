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
contaminante = 'PM10'
path = "{}_2020_{}.csv".format(mes,contaminante)
thisPath = Path(__file__).parent.absolute()
filePath = thisPath/'datos'/path
df = pd.read_csv(filePath)
#ABRIL
mes = '05'
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
#fig = decomposition.plot()
#plt.show()

#ARIMA
d = p = q = range(0,2)
pdq = list(itertools.product(p,d,q))

seasonal_pdq = [(x[0],x[1],x[2],12) for x in list(itertools.product(p,d,q))]

print("SARIMAX {} x {} ".format(pdq[1],seasonal_pdq[1]))
print("SARIMAX {} x {} ".format(pdq[1],seasonal_pdq[2]))
print("SARIMAX {} x {} ".format(pdq[2],seasonal_pdq[3]))
print("SARIMAX {} x {} ".format(pdq[2],seasonal_pdq[4]))
print(len(y))
warnings.filterwarnings("ignore")

for param in pdq:
    for param_seasonal in seasonal_pdq:
        try:
            mod = sm.tsa.statespace.SARIMAX(y,order=param,seasonal_order=param_seasonal,enforce_stationarity=False,enforce_invertibility=False)
            result = mod.fit()
            #print("ARIMA {} x {} 12 - AIC:{}".format(param,param_seasonal,result.aic))
        except:
            continue

mod = sm.tsa.statespace.SARIMAX(y,order=(1,1,1),seasonal_order=(1,1,1,4),enforce_stationarity=False,enforce_invertibility=False)
results = mod.fit()

print(results.summary().tables[1])

#results.plot_diagnostics(figsize=(16,8))
#plt.show()

#FORECASTING RIGHT?
pred = results.get_prediction(dynamic=False)
pred_ci = pred.conf_int()

ax = y['6':].plot(label='observed')
pred.predicted_mean.plot(ax=ax, label='prediccion',alpha=.7)
print("Predichos")
#Datos de prediccion pred_ci
#print(pred)
print(pred_ci)
ax.fill_between(pred_ci.index, pred_ci.iloc[:,0],pred_ci.iloc[:,1], color='k',alpha=.2)

ax.set_xlabel('Ho9ur')
ax.set_ylabel('Niveles PM10 i thing kfja')
plt.legend()
#plt.show()
print(ax)
#print(y)

y_forecasted = pred.predicted_mean
y_truth = y['0':]

mse = ((y_forecasted - y_truth) ** 2).mean()
print("Validacion de error : {}".format( round(mse,2) ) )

pred_uc = results.get_forecast(steps=500)
pred_ci = pred_uc.conf_int()