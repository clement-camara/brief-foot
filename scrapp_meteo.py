import requests
from bs4 import BeautifulSoup
import pandas as pd

from dict import thisdict, months
from scrapp_fonction import find_number

# création de l'url pour récupérer la meteo
city = 'Lille'
region = thisdict[city].lower()
city = city.lower()

mois_lettre = 'janvier'
mois_chiffre = months[mois_lettre]
# année = "2020"
# jours = "13"

url_test = f"https://www.historique-meteo.net/france/{region}/{city}//2020/05/02//"
print(url_test)

req = requests.get(url_test)
soup = BeautifulSoup(req.content, 'html.parser')
table = soup.find_all('table')
# creation du df avec toute les info meteo
df = pd.read_html(str(table))


# print(df)


def scrapp_degres_precipitation():
    # creation de varaible meteo necessaire
    temp_max = df[0][(df[0]['Unnamed: 0'] == 'Température maximale')]['01/05/2020']
    temp_min = df[0][(df[0]['Unnamed: 0'] == 'Température minimale')]['01/05/2020']
    precipitation = df[0][(df[0]['Unnamed: 0'] == 'Précipitations')]['01/05/2020']
    # transformation en integer
    temp_max = temp_max.apply(lambda x: find_number(x))
    temp_min = temp_min.apply(lambda x: find_number(x))
    precipitation = precipitation.apply(lambda x: find_number(x))
    # transformation en float
    temp_max = temp_max.astype('float64')
    temp_min = temp_min.astype('float64')
    precipitation = precipitation.astype('float64')
    # calcule de la temperature moyenne
    temperature = (temp_max.iloc[0] + temp_min.iloc[0]) / 2
    precipitation = precipitation.iloc[0]
    return temperature, precipitation


print(scrapp_degres_precipitation())


