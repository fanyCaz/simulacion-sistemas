from flask import Flask,render_template,request
import generadores.generadorMixto
import generadores.generadorMultiplicativo

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index(name=None):
    return render_template('index.html',name=name)

@app.route('/mixto',methods=['GET','POST'])
def mixto():
    if request.method == 'POST':
        x0 = int(request.form['mixto_x0'])
        a  = int(request.form['mixto_a'])
        c  = int(request.form['mixto_c'])
        m  = int(request.form['mixto_m'])
        periodo,nums = generadores.generadorMixto.numRectMixto(x0,a,c,m)
        return render_template('mixto.html',periodo=periodo,nums=nums)
    return render_template('mixto.html',periodo=None,nums=None)

@app.route('/multiplicativo',methods=['GET','POST'])
def multiplicativo():
    if request.method == 'POST':
        x0 = int(request.form['multiplicativo_x0'])
        a  = int(request.form['multiplicativo_a'])
        m  = int(request.form['multiplicativo_m'])
        periodo,nums = generadores.generadorMultiplicativo.numRectMultiplicativos(x0,a,m)
        return render_template('multiplicativo.html',periodo=periodo,nums=nums)
    return render_template('multiplicativo.html',periodo=None,nums=None)