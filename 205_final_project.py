from flask import Flask, render_template
from flask_bootstrap import Bootstrap4
from api import *

app = Flask(__name__)
bootstrap = Bootstrap4(app)

@app.route('/')
def home():
    return render_template('home.html')

random_drink = random_drink()
print(random_drink['drinks'][0]['strDrink']) # print name of drink
print('-------------')
for i in range(15): # 1-15 is all possible ingredients in each beverage
    ingredient = random_drink['drinks'][0]['strIngredient'+str(i+1)]
    if ingredient != None:
        print(ingredient)
