from flask import Flask,render_template,request
import informacion.Datos as dts

app = Flask(__name__)

@app.route('/')
def index(name=None):
    return render_template('index.html',name=name)

@app.route('/prueba')
def prueba():
    z = dts.prueba()
    return { "vals_prueba" : z }