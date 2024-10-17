import requests
from bs4 import BeautifulSoup

url = "https://exoplanetarchive.ipac.caltech.edu/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
confirmed_planets_div = soup.find('div', class_='stat')

if confirmed_planets_div:
    confirmed_planets = confirmed_planets_div.text.strip()
    print(f"Number of confirmed exoplanets: {confirmed_planets}")
else:
    print("Could not find the number of confirmed exoplanets on the page")
