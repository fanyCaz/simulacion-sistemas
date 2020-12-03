import numpy as np
import pandas as pd
import json
import csv
from pathlib import Path

def ValoresDeMes(mes: str, contaminante: str):
    #PATH PARA BASE DE DATOS
    path = "{}_2020_{}.csv".format(mes,contaminante)
    thisPath = Path(__file__).parent.absolute()
    filePath = thisPath/'datos'/path
    #OBTENCION DE DATOS
    datos = pd.read_csv(filePath,parse_dates=True, index_col=0)
    datosParaFechas = pd.read_csv(filePath)
    dFDatos = pd.DataFrame(datos)
    fechas = pd.DataFrame(datosParaFechas)['fecha']
    #SORTEAR POR FECHA
    nivelesAbril = dFDatos
    nivelesAbril = nivelesAbril.sort_values('fecha')
    y = nivelesAbril.mean()
    y = y.fillna(y.bfill())
    #PARA VALORES PREDICHOS
    pathPr = "promedios_{}.csv".format(contaminante)
    filePathPr = thisPath/pathPr
    datosPr = pd.read_csv(filePathPr,index_col=0)
    dFPrediccion = pd.DataFrame(datosPr)
    print( dFPrediccion.to_json() )

    niveles = y
    """
    print(niveles)
    print( int( niveles.argmax()) )
    print( max(niveles) )"""

    response = [
        {
            'fechas'  : fechas.to_json()
        },
        {
            'niveles' : niveles.to_json(),
            'predicciones' : dFPrediccion.to_json()
        },
        {
            'hora_maxima' : int(niveles.argmax()),
        }
    ]
    """ print( fechas )
    print( response ) """
    return response

#ValoresDeMes('05','PM10')