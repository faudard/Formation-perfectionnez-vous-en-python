# perfectionnez-vous-en-python avec OpenClassRooms

## Environnement virtuel et github
Command pour créer un nouvelle environnement virtuel
`virtualenv -p python3 env`

pour charger l'environnement
`source env/bin/activate`

Regarder la version de python 
`which python`


Ou les éléments de pip
`pip -V`

quitter l'environnement
`desactivate`

Pour clean l'environnement
`rm -rf env` 

Ajouter au gitignore l'environnement 
`echo env/ > .gitignore`
ou 
`echo env/ >> .gitignore`

Ajout des dépendances avec github
Creer un fichier requirement.txt puis ajouter les fichiers de dépendances puis pour les installer : 
`pip install -r requirements.txt` 
