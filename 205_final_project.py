'''
Course: CST 205 MULTIMEDIA DESIGN & PROGRAMMING
Title: 
Abstract:
Authors: David Eloy Saavedra, 
Date: 
'''

from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap5
from api import *

app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/drink', methods=['POST', 'GET'])
def drink():
    if(request.method == 'POST'):  # used for when user wants specific drink
        cocktail = cocktailByName(request.form.get("cocktailName")) # example margarita

        ingPrices = [] # prices of the ingredients
        for i in range(15): # 1-15 is all possible ingredients in each beverage
            ingredient = cocktail['drinks'][0]['strIngredient'+str(i+1)]
            if ingredient != None:
                ingPrices.append(getPrice(ingredient))
            else:
                break

        return render_template('drink.html', cocktail = cocktail, prices=ingPrices)
    else: # assumes user hit random, since "Random Drink" buttom or a tag is not in form tag
        cocktail = random_drink()

        ingPrices = [] # prices of the ingredients
        for i in range(15): # 1-15 is all possible ingredients in each beverage
            ingredient = cocktail['drinks'][0]['strIngredient'+str(i+1)]
            if ingredient != None:
                ingPrices.append(getPrice(ingredient))
            else:
                break

        return render_template('drink.html', cocktail = cocktail, prices=ingPrices)

# stop deleting
'''
how to run
$env:FLASK_APP = "205_final_project.py"
$env:FLASK_DEBUG = "1"
flask run
ctl + c
'''