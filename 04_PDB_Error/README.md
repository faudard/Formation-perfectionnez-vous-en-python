# perfectionnez-vous-en-python avec OpenClassRooms


## Utilisation de PDB 

Ajout de la library PDB et de l'instruction `pdb.set_trace()` dans le fichier parite.py

`import pdb ; pdb.set_trace()` 

Exécution du code pour csv (exemple)
`python parite.py -e csv`

Puis nouvelle console avec au début (Pdb), pour afficher l'extension par exemple `print(args.extension)`.

## Gestion des erreures 

Modification csv.py 
Ajout bloc try à l'ouverture du fichier 


Ajout a travers la librairie logging pour gérer le niveau des print
`import logging as lg`

puis exemple `lg.warning("Message {} ".format(e))`
Niveau de log :
1. CRITICAL problème très sérieux qui a pu causer l'arrêt du programme
1. Error cause d'un problème important le programme n'a pu réaliser une tâche
1. Warning quelque chose d'inattendu s'est produit mais que le produit continu de fonctionner
1. INFO info sur le programme
1. DEBUG info supplémentaire suite à une instruction
1. NOTSET


Pour activer le message du debug : 

`lg.basicConfig(level=lg.DEBUG)`


  













