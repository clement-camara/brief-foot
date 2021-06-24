CREATE TABLE championships (id INTEGER PRIMARY KEY AUTOINCREMENT,
name VARCHAR, country VARCHAR, start_year INTEGER, end_year INTEGER, created_at TIMESTAMP, updated_time TIMESTAMP);

CREATE TABLE teams (id INTEGER PRIMARY KEY AUTOINCREMENT,
championship_id INTEGER, name VARCHARD, city VARCHAR, coach_name VARCHAR, rank INTEGER, created_at TIMESTAMP, updated_at TIMESTAMP,
FOREIGN KEY(championship_id) REFERENCES championship(id));

CREATE TABLE players (id INTEGER PRIMARY KEY AUTOINCREMENT,
first_name VARCHAR, last_name VARCHAR, birthdate DATE, team_id INTEGER, position VARCHAR, nationality VARCHAR, created_at TIMESTAMP, update_at TIMESTAMP,
FOREIGN KEY(team_id) REFERENCES teams(id));

CREATE TABLE goals (id INTEGER PRIMARY KEY AUTOINCREMENT,
match_id INTEGER, player_id INTEGER, goal_type VARCHAR, created_at TIMESTAMPS, update_at TIMESTAMPS,
FOREIGN KEY (player_id) REFERENCES players(id),FOREIGN key (match_id) REFERENCES matchs(id));

CREATE TABLE matchs(id INTEGER PRIMARY KEY AUTOINCREMENT,
date DATIME, place VARCHAR, rainfall FLOAT, temperature FLOAT, created_at TIMESTAMP, updated_at TIMESTAMP);

CREATE TABLE teams_matches ( id INTEGER PRIMARY KEY AUTOINCREMENT,
match_id INTEGER, team_id INTEGER, home BOOLEAN, team_goals INTEGER, points INTEGER, created_at TIMESTAMP, update_at TIMESTAMP,
FOREIGN KEY (team_id) REFERENCES teams(id),FOREIGN KEY (match_id) REFERENCES matchs(id));