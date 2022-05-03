import requests

def cocktail(drink):
<<<<<<< HEAD
    return requests.get(f"https://www.thecocktaildb.com/api/json/v1/1/search.php?s={drink}").json()

def random_drink():
    return requests.get(f"https://www.thecocktaildb.com/api/json/v1/1/random.php").json()
=======
    response = requests.get(f"https://www.thecocktaildb.com/api/json/v1/1/search.php?s={drink}")
    # print(response.status_code)
    return response.json()

def cocktailRandom():
    response = requests.get(f"https://www.thecocktaildb.com/api/json/v1/1/random.php")
    # print(response.status_code)
    return response.json()
>>>>>>> f024e279ad41be4fa882a99e0331f9163a1d73df
