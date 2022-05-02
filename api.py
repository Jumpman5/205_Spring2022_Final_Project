import requests

def cocktail(drink):
    response = requests.get(f"https://www.thecocktaildb.com/api/json/v1/1/search.php?s={drink}")
    # print(response.status_code)
    return response.json()

def cocktailRandom():
    response = requests.get(f"https://www.thecocktaildb.com/api/json/v1/1/random.php")
    # print(response.status_code)
    return response.json()