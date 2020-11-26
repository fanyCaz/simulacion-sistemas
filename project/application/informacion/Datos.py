import numpy as np
import pandas as pd
import json
import csv
from pathlib import Path

def ValoresDeMes(mes: int, contaminante: str):
    path = "{}_2020_{}.csv".format(mes,contaminante)
    thisPath = Path(__file__).parent.absolute()
    filePath = thisPath/'datos'/path
    datos = pd.read_csv(filePath)
    dFDatos = pd.DataFrame(datos)
    fechas = dFDatos['fecha']
    niveles = dFDatos.loc[0:,'0':'23']
    response = [
        {
        'fechas'  : fechas.to_json()
        },
        {
        'niveles' : niveles.to_json()
        }
    ]
    """ print( fechas )
    print( response ) """
    return response