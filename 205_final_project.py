'''
Course: CST 205 MULTIMEDIA DESIGN & PROGRAMMING
Title: Cocktail Finder
Abstract: This program creates a website that people can use to search for cocktails by name/ingredient
    or find a random cocktail. The site displays price information scraped from Amazon Fresh, giving users
    a total price for a given cocktail, as well as the ability to click on ingredients and be redirected
    to the Amazon website.
Authors: David Eloy Saavedra, Nico Hartojo, Tyler Johnson-Haro
Date: 5/16/22
github link: https://github.com/Jumpman5/205_Spring2022_Final_Project

Trello link: https://trello.com/b/NcVZxl8s/cst205-final-proj
'''

from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap5
from api import *

app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route('/') # home page with the random and certain drink button
def home(): 
    return render_template('home.html')

@app.route('/drink', methods=['POST', 'GET']) # from home page depending on which button was push it either does POST or GET
def drink():
    if(request.method == 'POST'):  # used for when user wants specific drink
        cocktail = cocktailByName(request.form.get("cocktailName")) # example margarita
        ingPrices,links,total_price = getPriceAndLinks(cocktail)

        return render_template('drink.html', cocktail = cocktail, prices=ingPrices, links=links, total=round(total_price,2))
    else: # assumes user hit random, since "Random Drink" buttom or a tag is not in form tag
        cocktail = random_drink()
        ingPrices,links,total_price = getPriceAndLinks(cocktail)

        return render_template('drink.html', cocktail=cocktail, prices=ingPrices, links=links, total=round(total_price,2))

# returns list of ingredient prices, list of Amazon links for those ingredients, and total price of ingredients
def getPriceAndLinks(cocktail):
    ingPrices = [] # prices of the ingredients
    links = []
    for i in range(15): # 1-15 is all possible ingredients in each beverage
        ingredient = cocktail['drinks'][0]['strIngredient'+str(i+1)]
        if ingredient != None:
            temp = getPrice(ingredient)
            ingPrices.append(temp[0])
            links.append(temp[1])
        else:
            break
    total_price = 0
    for price in ingPrices:
        # make sure that price information was found from scraping
        if (type(price) != str):
            total_price += float(price[1:])
    return ingPrices,links,total_price

'''
how to run
$env:FLASK_APP = "205_final_project.py"
$env:FLASK_DEBUG = "1"
flask run
ctl + c

export FLASK_APP=205_final_project.py
export FLASK_DEBUG=1
flask run
'''
