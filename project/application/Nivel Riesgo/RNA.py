import pandas as pd
import numpy as np
from sklearn.neural_network import MLPRegressor

datosCO = pd.read_csv("CO.csv")
x=datosCO["Niveles"]
y=datosCO["Limite"]
#------------------------------
datosPM10 = pd.read_csv("PM10.csv")
x1=datosPM10["Niveles"]
y1=datosPM10["Limite"]
#------------------------------
datosPM25 = pd.read_csv("PM2.5.csv")
x2=datosPM25["Niveles"]
y2=datosPM25["Limite"]
#------------------------------
datosSO2 = pd.read_csv("SO2.csv")
x3=datosSO2["Niveles"]
y3=datosSO2["Limite"]
#------------------------------
datosNO2 = pd.read_csv("NO2.csv")
x4=datosNO2["Niveles"]
y4=datosNO2["Limite"]
#------------------------------
datosOZONO = pd.read_csv("OZONO.csv")
x5=datosOZONO["Niveles"]
y5=datosOZONO["Limite"]

X=x[:,np.newaxis]
X1=x1[:,np.newaxis]
X2=x2[:,np.newaxis]
X3=x3[:,np.newaxis]
X4=x4[:,np.newaxis]
X5=x5[:,np.newaxis]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y)
X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1)
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2)
X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3)
X4_train, X4_test, y4_train, y4_test = train_test_split(X4, y4)
X5_train, X5_test, y5_train, y5_test = train_test_split(X5, y5)

mlr=MLPRegressor(solver='lbfgs',alpha=1e-5,hidden_layer_sizes=(3,3),random_state=1)
mlr1=MLPRegressor(solver='lbfgs',alpha=1e-5,hidden_layer_sizes=(3,3),random_state=1)
mlr2=MLPRegressor(solver='lbfgs',alpha=1e-5,hidden_layer_sizes=(3,3),random_state=1)
mlr3=MLPRegressor(solver='lbfgs',alpha=1e-5,hidden_layer_sizes=(3,3),random_state=1)
mlr4=MLPRegressor(solver='lbfgs',alpha=1e-5,hidden_layer_sizes=(3,3),random_state=1)
mlr5=MLPRegressor(solver='lbfgs',alpha=1e-5,hidden_layer_sizes=(3,3),random_state=1)
mlr.fit(X_train, y_train)
mlr1.fit(X1_train, y1_train)
mlr2.fit(X2_train, y2_train)
mlr3.fit(X3_train, y3_train)
mlr4.fit(X4_train, y4_train)
mlr5.fit(X5_train, y5_train)

print("Prediccion de CO: ", mlr.predict([[11]]))
print("Prediccion de PM10: ", mlr1.predict([[75]]))
print("Prediccion de PM2.5: ", mlr2.predict([[45]]))
print("Prediccion de SO2: ", mlr3.predict([[10]]))
print("Prediccion de NO2: ", mlr4.predict([[21]]))
print("Prediccion de OZONO: ", mlr5.predict([[61]]))