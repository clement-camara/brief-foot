import pandas as pd
import requests
from bs4 import BeautifulSoup

def scrapp_teams():
    '''Récupération des tableaux des pages équipes
    Retourne une liste de listes de dataframe,
    chaque liste correspond a une équipe,
    chaque dataframe correspond a un tableau concernant cette équipe'''
    # Récupération des liens des pages
    URL = 'https://www.lequipe.fr/Football/ligue-1/page-participants'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find_all('ul', class_='clubs')
    list_url_clubs = []
    for result in results:
        liens_clubs = result.find_all('ul', class_='club-links')
        for liens in liens_clubs:
            list_url_clubs.append(liens)
    list_liens = []
    for club in list_url_clubs:
        lien = club.find('a', class_='link')
        list_liens.append(lien.get('href'))
    # Scrapping des tableaux
    list_dfs = []
    for lien in list_liens :
        dfs = pd.read_html(f'https://www.lequipe.fr{lien}')
        list_dfs.append(dfs)
    return list_dfs


def scrapp_rank():
    '''Récupère le classement global du championnat
    Retourne un dataframe avec le nombre de points par équipe'''
    df_classement = pd.read_html(
        'https://www.lequipe.fr/Football/ligue-1/saison-2020-2021/page-classement-equipes/general')[0]
    df_classement = df_classement.rename(columns={'Unnamed: 1': 'Equipe'})
    df_rank = df_classement[['Equipe', 'pts']]
    return df_rank
