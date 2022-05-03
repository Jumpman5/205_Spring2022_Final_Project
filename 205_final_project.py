#Final Project Starter File Test 1 Test 2
from flask import Flask, render_template
from flask_bootstrap import Bootstrap4

from api import *

# print(cocktailRandom())
# print(cocktail('margarita'))

app = Flask(__name__)
bootstrap = Bootstrap4(app)

@app.route('/')
def home():
    return render_template('home.html')




'''
how to run

$env:FLASK_APP = "205_final_project.py"
$env:FLASK_DEBUG = "1"
flask run

ctl + c
'''