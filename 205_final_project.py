from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap5
from api import *
from bs4 import BeautifulSoup
from urllib.request import urlopen
from distutils.filelist import findall
import ssl
#ssl._create_default_https_context = ssl._create_unverified_context
#my_site='https://www.airnow.gov/?city=Monterey&state=CA&country=USA'
#site_html=urlopen(my_site)
# print out a portion of the HTML
#print(site_html.read()[5000:5400])
target_html = urlopen('https://www.target.com/s?searchTerm=almond+milk')
#print(target_html.read()[0:10000])
data = BeautifulSoup(target_html, 'lxml')

#for i in data.findAll('img'):
    #print(i.attrs['src'])

#for i in data.findAll('span'):
    #print(i.attrs['class'])
#use beautiful soup for reading specific tags like <span>$3.19</span>
# print(cocktailRandom())
# print(cocktail('margarita'))

app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route('/')
def home():
    return render_template('home.html')

#random_drink = random_drink()
#print(random_drink['drinks'][0]['strDrink']) # print name of drink
#print('-------------')
#for i in range(15): # 1-15 is all possible ingredients in each beverage
    #ingredient = random_drink['drinks'][0]['strIngredient'+str(i+1)]
    #if ingredient != None:
        #print(ingredient)
        #1
@app.route('/drink', methods=['POST', 'GET'])
def drink():
    if(request.method == 'POST'):  # used for when user wants specific drink
        cocktail = cocktailByName(request.form.get("cocktailName")) # example margarita

        ingPrices = [] # prices of the ingredients
        ing = [] # ingredients
        for i in range(15): # 1-15 is all possible ingredients in each beverage
            ingredient = cocktail['drinks'][0]['strIngredient'+str(i+1)]
            if ingredient != None:
                ingPrices.append(getPrice(ingredient))
                ing.append(ingredient)
            else:
                break

        return render_template('drink.html', cocktail = cocktail, prices=ingPrices)
    else: # assumes user hit random, since "Random Drink" buttom or a tag is not in form tag
        cocktail = random_drink()

        ingPrices = [] # prices of the ingredients
        ing = [] # ingredients
        for i in range(15): # 1-15 is all possible ingredients in each beverage
            ingredient = cocktail['drinks'][0]['strIngredient'+str(i+1)]
            if ingredient != None:
                ingPrices.append(getPrice(ingredient))
                ing.append(ingredient)
            else:
                break

        return render_template('drink.html', cocktail = cocktail, prices=ingPrices)



#how to run
#$env:FLASK_APP = "205_final_project.py"
#$env:FLASK_DEBUG = "1"
#flask run
#ctl + c
