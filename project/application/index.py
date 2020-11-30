from flask import Flask,render_template,request
import informacion.Datos as dts

app = Flask(__name__)

@app.route('/')
def index(name=None):
    return render_template('index.html',name=name)

@app.route('/mes/<mes>/<contaminante>', methods=['GET'])
def datosMes(mes:int,contaminante:str):
    response = {}
    if request.method == 'GET':
        print( f"mes pedido {mes} y contaminante {contaminante}" )
        response = { 'Datos' : dts.ValoresDeMes(mes,contaminante) }
        return response
    else:
        response = {'Datos' : []}
        return response

@app.route('/prediccion/<mes>/<contaminante>',methods=['GET'])
def prediccionMes(mes:int,contaminante:str):
    response = 1
    return response