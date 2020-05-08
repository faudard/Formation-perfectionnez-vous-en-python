# perfectionnez-vous-en-python avec OpenClassRooms

## Avant-propos
faire le `source env/bin/activate`

`pip install numpy`
`pip install matplotlib`
`pip install pandas`

Par rapport au tuto j'ai du installé pour matplotlib :
`sudo apt-get install python3-tk`
tkinder 
Aussi : 
`pip install seaborn`

## Utilisation de numpy 
simple `import numpy as np`

## Utilisation de pandas 
simple `import pandas as pd`
Après on utilise les dataFrame que l on note après df en raccourci
`famille_panda_df = pd.DataFrame(famille_panda)`

## Utilisation de matplotlib
simple import `matplotlib.pyplot as plt`

## Resumé 
Bloc a mettre : 


Modification csv.py 
Ajout bloc try à l'ouverture du fichier 


Ajout a travers la librairie logging pour gerer le niveau des print
`import logging as lg`

puis exemple `lg.warning("Message {} ".format(e))`
Niveau de log : 
1. CRITICAL problème très serieux qui a pu causer l'arrêt du programme 
1. Error cause d'un problème important le programme n'a pu réaliser une tâche
1. Warning quelque chose d'inattendu c'est produit mais que le produit continu de fonctionner 
1. INFO info sur le programme 
1. DEBUG info supplémentaire suite à une instruction
1. NOTSET


Pour activer le message du debug : 

`lg.basicConfig(level=lg.DEBUG)`


  













