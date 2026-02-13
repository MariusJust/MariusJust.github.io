from flask import Flask, render_template

app = Flask(__name__)
app.config['EXPLAIN_TEMPLATE_LOADING'] = True 


@app.route('/')
def index():
    
    return render_template("index.html")

@app.route('/neuralnet')
def neuralnet():
    return render_template("NeuralNet.html")

@app.route('/DGPE_Køge')
def dgpe_koege():
    return render_template("DGPE.html")

@app.route('/P_Project')
def p_project():
    return render_template("P_Project.html")

