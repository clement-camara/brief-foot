import requests
from bs4 import BeautifulSoup
import pandas as pd

from dict import thisdict, months

# création de l'url pour récupérer la meteo
city = 'Nice'
region = thisdict[city].lower()
city = city.lower()
mois_lettre = 'juillet'
mois_chiffre = months[mois_lettre]
year = "2019"
day = "19"


def scrapp_time(city, region, mois_chiffre, year, day):
    url = f"https://www.historique-meteo.net/france/{region}/{city}//{year}/{mois_chiffre}/{day}//"
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    table = soup.find_all('table')
    # creation du df avec toute les info meteo
    df = pd.read_html(str(table))
    df = df[0]
    df = df.rename(columns={df.columns[3]: 'Date_day'})
    df2 = df.rename(columns={df.columns[0]: 'info'})
    # récupération temp max, min et precipitation
    Température_maximale = df2.Date_day.head(1)[0].split('°')[0]
    Température_minimale = df2.Date_day.head(2)[1].split('°')[0]
    Précipitations = df2.Date_day.head(5)[4].split('mm')[0]
    # transformation en float
    Température_maximale = float(Température_maximale)
    Température_minimale = float(Température_minimale)
    Précipitations = float(Précipitations)
    # calcule de la temperature moyenne
    temperature = (Température_maximale + Température_minimale) / 2
    return f'La températures moyenne a {city} le {day} {mois_lettre} {year}  ' \
           f'est de: {temperature}° et les précipitaions de: {Précipitations} mm. '


print(scrapp_time(city, region, mois_chiffre, year, day))


