import json
from datetime import date
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

@app.route('/First_Year')
def first_year():
    return render_template("First_Year.html")

@app.route('/jobbank')
def jobbank():
    with open('data/jobs.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    today = date.today().isoformat()
    active_jobs = [j for j in data['jobs'] if j.get('deadline', '9999-99-99') >= today]
    companies = data.get('companies', [])
    return render_template("jobbank.html", jobs=active_jobs, companies=companies)
