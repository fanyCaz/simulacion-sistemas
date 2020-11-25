import numpy as np
import pandas as pd
import json
import csv

def ValoresDeMes(mes: int):
    path = "./static/datos/{}".format(mes)
    print(path)
    return 1