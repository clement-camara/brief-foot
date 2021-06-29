import sqlite3
import pandas as pd

# Connection à la db, crée le fichier s'il n'existe pas déjà
conn = sqlite3.connect('db_foot.sqlite3')
c = conn.cursor()


# Requètes de creation des différentes tables
championships = '''CREATE TABLE IF NOT EXISTS championships (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR,
    country VARCHAR,
    start_year INTEGER,
    end_year INTEGER,
    created_at TIMESTAMP,
    updated_at TIMESTAMP)'''
teams = '''CREATE TABLE IF NOT EXISTS teams (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    championship_id INTEGER,
    name VARCHARD,
    city VARCHAR,
    coach_name VARCHAR,
    rank INTEGER,
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    FOREIGN KEY(championship_id) REFERENCES championships(id))'''
players = '''CREATE TABLE IF NOT EXISTS players (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR,
    last_name VARCHAR,
    birthdate DATE,
    team_id INTEGER,
    position VARCHAR,
    nationality VARCHAR,
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    FOREIGN KEY(team_id) REFERENCES teams(id))'''
goals = '''CREATE TABLE IF NOT EXISTS goals (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    match_id INTEGER,
    player_id INTEGER,
    goal_type VARCHAR,
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    FOREIGN KEY (player_id) REFERENCES players(id),
    FOREIGN KEY (match_id) REFERENCES matchs(id))'''
matchs = '''CREATE TABLE IF NOT EXISTS matchs(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date DATIME,
    place VARCHAR,
    rainfall FLOAT,
    temperature FLOAT,
    created_at TIMESTAMP,
    updated_at TIMESTAMP)'''
teams_matches = '''CREATE TABLE IF NOT EXISTS teams_matches (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    match_id INTEGER,
    team_id INTEGER,
    home BOOLEAN,
    team_goals INTEGER,
    points INTEGER,
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    FOREIGN KEY (team_id) REFERENCES teams(id)
    FOREIGN KEY (match_id) REFERENCES matchs(id))'''


# Fonctions de création et de suppression de table
def create_table(query):
    '''Create table from query specified'''
    c.execute(query)
    conn.commit()

def drop_table(table_name):
    '''Drop table specified'''
    c.execute('''DROP TABLE %s''' % (table_name,))
    conn.commit()


# Fonction d'insertion
def add_championship(name, country, start_year, end_year):
    '''Add championship in table championships with values specified'''
    c.execute('''INSERT INTO championships (name, country, start_year, end_year, created_at, updated_at) VALUES (?, ?, ?, ?, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)''', (name,country,start_year,end_year))
    conn.commit()


# Version pandas
def insert_table(my_df, my_table):
  '''Insert Dataframe into table specified'''
  my_df.to_sql(my_table, conn, if_exists='append', index=False)

def read_db(my_query):
  '''Read sql query, read the db an return response in a dataframe'''
  df = pd.read_sql(my_query, conn)
  return df


#Sandbox
# drop_table('championships')
# create_table(championships)
# create_table(matchs)
# create_table(teams)
# create_table(players)
# create_table(goals)
# create_table(teams_matches)

# add_championship('Ligue 1', 'France', 2020, 2021)


# Lis le contenu de la table
df_championships = read_db('''SELECT * FROM championships''')
df_championships


# Recup id et nom dans un dict
championships_dict = {}
for championship in range(len(df_championships)):
    championship_dict = {df_championships.iloc[championship,1] : df_championships.iloc[championship, 0]}
    championships_dict.update(championship_dict)
championships_dict

# map colonne avec dictionnaire des ids
df_teams['championship_id'] = df_teams['championship'].map(championships_dict)
df_teams

