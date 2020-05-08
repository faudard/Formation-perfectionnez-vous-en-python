import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt

class SetOfParliamentMembers: 
     def __init__(self,name): 
         self.name = name 
     # 
     def data_from_csv(self, csv_file):
         self.dataframe = pd.read_csv(csv_file, sep=";")
     # 
     def data_from_dataframe(self, dataframe):
         self.dataframe = dataframe
     # 
     def split_by_political_party(self): 
         result = {}
         data = self.dataframe
         # 
         all_parties = data["parti_ratt_financier"].dropna().unique() # dropna supprime les NaN unique les doublons
         # 
         for party in all_parties:
             data_subset = data[data.parti_ratt_financier == party]
             subset = SetOfParliamentMembers('MPS from party "{}"'.format(party))
             subset.data_from_dataframe(data_subset)
             result[party] = subset 
         # 
         return result
     # 
     def display_chart(self):
         #print(self.dataframe)
         data = self.dataframe 
         female_mps = data[data.sexe == "F"]
         male_mps = data[data.sexe == "H"] # H et non M ... 
         # 
         #print(data.sexe)
         #print(len(female_mps),len(male_mps))
         counts = [len(female_mps), len(male_mps)]
         counts = np.array(counts)
         nb_mps = counts.sum()
         #
         proportions = counts / nb_mps
         # 
         labels = ["Female ({})".format(counts[0]), "Male ({})".format(counts[1])]  
         fig, ax = plt.subplots()
         ax.axis("equal")
         ax.pie(proportions,labels = labels, autopct = "%1.1f pourcents")
         plt.title("{} ({} MPs)".format(self.name, nb_mps))
         plt.show()


import seaborn as sns

import os 
data_file ='current_mps.csv'

def launch_analysis(data_file, by_party=False) : 
    sopm = SetOfParliamentMembers('All MPs') # dans le tuto sopm
    sopm.data_from_csv(os.path.join('data/',data_file))
    sopm.display_chart()
    #
    if by_party : 
        for party, s in sopm.split_by_political_party().items(): 
            print(party,s)
            s.display_chart()
#    else : 

launch_analysis(data_file,by_party=True)


#launch_analysis(data_file,by_party=False)


