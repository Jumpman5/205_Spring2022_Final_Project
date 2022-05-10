import requests
from bs4 import BeautifulSoup

def cocktailByName(drink):
    return requests.get(f"https://www.thecocktaildb.com/api/json/v1/1/search.php?s={drink}").json()

def random_drink():
    return requests.get(f"https://www.thecocktaildb.com/api/json/v1/1/random.php").json()

def getPrice(item): # gets first result price from amazon fresh
    cookies = {'session': '131-1062572-6801904'} # need this now ???? but it works now originally 131-1062572-6801905
    # header = { # keep just in case
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    # }
    header = ({'User-Agent':
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
        'Accept-Language': 'en-US, en;q=0.5'})
    url = f"https://www.amazon.com/s?k={item}&i=amazonfresh"
    print(url)
    webpage = requests.get(url, headers=header, cookies=cookies)
    soup = BeautifulSoup(webpage.content, "lxml")

    title = "Price information not found"
    found = soup.find("span", attrs={"class":'a-offscreen'})
    if found:
        title = found.string
    return title
    
