import requests
from bs4 import BeautifulSoup

def cocktailByName(drink):
    return requests.get(f"https://www.thecocktaildb.com/api/json/v1/1/search.php?s={drink}").json()

def random_drink():
    return requests.get(f"https://www.thecocktaildb.com/api/json/v1/1/random.php").json()

def getPrice(item): # gets first result price from amazon fresh
    HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})
    URL = f"https://www.amazon.com/s?k={item}&i=amazonfresh"
    webpage = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(webpage.content, "lxml")
    title = soup.find("span", attrs={"class":'a-offscreen'}).string
    return title
    
