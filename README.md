# brief-foot

1ère étape: Live-code d’une demi heure sur la conception d’une architecture DB faite par l’encadrant Les notions développées:
CRUD SQL
​

2ème étape: Avec le même groupe que l’atelier précédent, les apprenants créent une DB sqlite3 avec la structure définie au dessus et doivent la remplir de deux manières:
Un scrapper sur https://www.lequipe.fr/Football/ligue-1/page-calendrier-resultats et les pages associées pour les données liées au foot.
Un call API sur https://openweathermap.org/ pour les données liées à la météo. Vous pouvez bien-sur enrichir votre base de données de toutes les ressources qui vous semblent pertinentes.

Premier pas sur le projet:

1) cloner le repo brief-foot
- git clone https://github.com/clement-camara/brief-foot
3) récupérer l'environnement de travail conda avec le fichier .yml:
- conda env create -f environment.yml
- conda activate environnement
Si d'autres dépendances sont ajoutées/supprimées , mettre à jour le .yml à l'aide de la commande
conda env export --from-history > environment.yml