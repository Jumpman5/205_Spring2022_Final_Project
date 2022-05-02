#Final Project Starter File Test 1 Test 2
from flask import Flask, render_template
from flask_bootstrap import Bootstrap4

app = Flask(__name__)
bootstrap = Bootstrap4(app)

@app.route('/')
def home():
    return render_template('home.html')