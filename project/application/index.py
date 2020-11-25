from flask import Flask,render_template,request
import informacion.Datos as dts

app = Flask(__name__)

@app.route('/')
def index(name=None):
    return render_template('index.html',name=name)

@app.route('/mes/<mes>', methods=['GET'])
def datosMes(mes):
    mesRec = mes
    response = {}
    if request.method == 'GET':
        print(mesRec)
        response = { 'Datos' : dts.ValoresDeMes(mesRec) }
        return response
    else:
        response = {'Datos' : []}
        return response