import numpy as np
import pandas as pd
import json
import csv
from pathlib import Path

def ValoresDeMes(mes: str, contaminante: str):
    path = "{}_2020_{}.csv".format(mes,contaminante)
    thisPath = Path(__file__).parent.absolute()
    filePath = thisPath/'datos'/path
    datos = pd.read_csv(filePath,parse_dates=True, index_col=0)
    datosParaFechas = pd.read_csv(filePath)
    dFDatos = pd.DataFrame(datos)
    fechas = pd.DataFrame(datosParaFechas)['fecha']
    
    nivelesAbril = dFDatos
    nivelesAbril = nivelesAbril.sort_values('fecha')
    y = nivelesAbril.mean()
    y = y.fillna(y.bfill())
    #print(y.to_json())
    #print(fechas)
    
    niveles = y
    print(niveles)
    print( int( niveles.argmax()) )
    print( max(niveles) )
    #niveles = dFDatos.loc[0:,'0':'23']
    response = [
        {
            'fechas'  : fechas.to_json()
        },
        {
            'niveles' : niveles.to_json()
        },
        {
            'hora_maxima' : int(niveles.argmax()),
        }
    ]
    """ print( fechas )
    print( response ) """
    return response

ValoresDeMes('05','PM10')