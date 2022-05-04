from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from api import *

from api import *

# print(cocktailRandom())
# print(cocktail('margarita'))

app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/drink')
def drink():
    return render_template('drink.html')

random_drink = random_drink()
print(random_drink['drinks'][0]['strDrink']) # print name of drink
print('-------------')
for i in range(15): # 1-15 is all possible ingredients in each beverage
    ingredient = random_drink['drinks'][0]['strIngredient'+str(i+1)]
    if ingredient != None:
        print(ingredient)



'''
how to run

$env:FLASK_APP = "205_final_project.py"
$env:FLASK_DEBUG = "1"
flask run

ctl + c
'''
