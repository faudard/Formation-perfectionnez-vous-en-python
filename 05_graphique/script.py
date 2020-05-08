#!/bin

"""
Exemple tableau
		pattes 	poil 	queue 	ventre 
maman_panda	100 	5	20	80
bébé_panda	50	2.5	10	40
papa_panda	110	6	22	80
"""
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 

# test pandas 
un_panda = [100, 5,20, 50]


un_panda_numpy = np.array(un_panda)
k = 2

un_bebe_panda_numpy = un_panda_numpy / k



famille_panda = [
    [100, 5  , 20, 80], # maman panda
    [50 , 2.5, 10, 40], # bb 
    [110, 6  , 22, 80], # papa
]

print(type(famille_panda))

famille_panda_numpy = np.array(famille_panda)

print(type(famille_panda_numpy))

# pandas 
famille_panda_df = pd.DataFrame(famille_panda)

print(famille_panda_df)
# Ajout des index ; columns
 
famille_panda_df = pd.DataFrame(famille_panda_numpy,
                                 index = ['maman', 'bebe', 'papa'],
                                 columns = ['pattes', 'poil', 'queue', 'ventre'])

print(famille_panda_df.ventre)
print(famille_panda_df["ventre"].values)


for line in famille_panda_df.iterrows():
    index_line = line[0]
    contains_line = line[1]
    print('Papa %s:' % index_line)
    print(contains_line)
    print('--------------------------')

print('\n')
print('\n')
print('\n')
# pour les accès on utilise iloc / loc : 
print(famille_panda_df.iloc[1])
print(famille_panda_df.loc['bebe'])

# Test si 80 
print(famille_panda_df["ventre"] == 80)



#mask = famille_panda_df["ventre"] == 80
#pandas_80 = famille_panda_df[mask]

pandas_80 = famille_panda_df[famille_panda_df["ventre"] == 80]
print(pandas_80)

# not avec ~
mask = famille_panda_df["ventre"] == 80
pandas_not_80 = famille_panda_df[~mask]
print(pandas_not_80)



quelques_pandas = pd.DataFrame([[105,4,19,80],[100,5,20,80]],      # deux nouveaux pandas
                                columns = famille_panda_df.columns) 
                                # même colonnes que famille_panda_df
tous_les_pandas = famille_panda_df.append(quelques_pandas)
print(tous_les_pandas)


# pour enlever les doublons 
tous_les_pandas = tous_les_pandas.drop_duplicates()

# accéder aux noms des colonnes
famille_panda_df.columns

# créer une nouvelle colonne, composée de chaînes de caractères
famille_panda_df["sexe"] = ["f", "f", "m"]

# obtenir le nombre de lignes
len(famille_panda_df)

# mps = pd.read_csv("data/current_mps.csv", sep=";")
