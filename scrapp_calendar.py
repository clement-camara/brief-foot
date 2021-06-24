import pandas as pd
import requests
from bs4 import BeautifulSoup

def scrapp_matchs():
    '''Fonction pour scrapper tout les matchs'''
    # Récupération des urls des pages des journées du championnat
    URL = 'https://www.lequipe.fr/Football/ligue-1/saison-2020-2021/page-calendrier-resultats'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find_all('select', class_='SelectNav__select')
    list_url_journey = []
    for result in results:
        liens_journey = result.find_all('option')
        for liens in liens_journey:
            list_url_journey.append(liens.get('value'))
    # Récupération des données pour chaque match
    row_list = []
    for url_journey in list_url_journey:
        journey = pd.read_json(url_journey, lines=True)
        for match in journey['items'][0]:
            try:
                if len(match['items']) == 1:
                    match_dict={}
                    match_dict['place'] = match['items'][0]['event']['lieu']['ville']
                    match_dict['date'] = match['items'][0]['event']['date']
                    match_dict['dom_name'] = match['items'][0]['event']['specifics']['domicile']['equipe']['nom']
                    match_dict['ext_name'] = match['items'][0]['event']['specifics']['exterieur']['equipe']['nom']
                    match_dict['but_dom'] = match['items'][0]['event']['specifics']['score']['domicile']
                    match_dict['but_ext'] = match['items'][0]['event']['specifics']['score']['exterieur']
                    match_dict['winner'] = match['items'][0]['event']['specifics']['vainqueur']
                    match_dict['lien'] = match['items'][0]['event']['lien_web']
                    row_list.append(match_dict)
                elif len(match['items']) > 1:
                    for m in range(len(match['items'])):
                        match_dict={}
                        match_dict['place'] = match['items'][m]['event']['lieu']['ville']
                        match_dict['date'] = match['items'][m]['event']['date']
                        match_dict['dom_name'] = match['items'][m]['event']['specifics']['domicile']['equipe']['nom']
                        match_dict['ext_name'] = match['items'][m]['event']['specifics']['exterieur']['equipe']['nom']
                        match_dict['but_dom'] = match['items'][m]['event']['specifics']['score']['domicile']
                        match_dict['but_ext'] = match['items'][m]['event']['specifics']['score']['exterieur']
                        match_dict['winner'] = match['items'][m]['event']['specifics']['vainqueur']
                        match_dict['lien'] = match['items'][m]['event']['lien_web']
                        row_list.append(match_dict)
            except:
                pass
    # Stockage en dataframe
    data = pd.DataFrame(row_list)
    return data

data = scrapp_matchs()
list_liens_matchs = data['lien'].tolist()
list_liens_matchs



