from flask import Flask, render_template
from browniano import generator
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')
    

@app.route("/brownian-values")
def brownianValues():
    res = generator()
    pos_values = res[0]
    mayor = res[1]
    return { "pos_values": pos_values,"mayor": mayor }