from flask import Flask, render_template
import os


app = Flask(__name__)
app.config['EXPLAIN_TEMPLATE_LOADING'] = True 


@app.route('/')
def index():
    
    return render_template("index.html")

@app.route('/neuralnet')
def neuralnet():
    return render_template("NeuralNet.html")