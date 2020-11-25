import numpy as np
import pandas as pd
import json
import csv
from pathlib import Path

def ValoresDeMes(mes: int, contaminante: str):
    path = "{}_2020_{}.csv".format(mes,contaminante)
    thisPath = Path(__file__).parent.absolute()
    filePath = thisPath/'datos'/path
    #Obtener path de archivo
    """print( thisPath )
    print(filePath)
    print(filePath.exists())"""
    datos = pd.read_csv(filePath)
    dFDatos = pd.DataFrame(datos)
    print(dFDatos)
    print( type(dFDatos) )
    return 1