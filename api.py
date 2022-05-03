import requests

def cocktail(drink):
    return requests.get(f"https://www.thecocktaildb.com/api/json/v1/1/search.php?s={drink}").json()

def random_drink():
    return requests.get(f"https://www.thecocktaildb.com/api/json/v1/1/random.php").json()
