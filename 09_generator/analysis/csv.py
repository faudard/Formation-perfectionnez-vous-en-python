#!/usr/bin/env python3 
#coding: utf-8 

import os 
import logging as lg
import pandas as pd 
import numpy as np 

import matplotlib.pyplot as plt 
import seaborn as sns



AGE_COLUMN_NAME = "age"                 # Name of the new column (containing the age of the MP)
                                        # to create in the dataframe
AGE_YEARS_COLUMN_NAME = "age_in_years"
BIRTH_COLUMN_NAME = "birth"

MINIMUM_MP_AGE = 18




class SetOfParliamentMembers: 
    ALL_REGISTERED_PARTIES = [] # This is a class attribute
    def __init__(self,name): 
        self.name = name 
    # 
    def data_from_csv(self, csv_file):
        self.dataframe = pd.read_csv(csv_file, sep=";")
    # On peut supprimer la fonction suivant mais j ai gardé pour la forme
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
    def split_by_age(self, age_split):
        data = self.dataframe
        self._compute_age_column()
        self.display_histogram(data[AGE_YEARS_COLUMN_NAME].values)
        #  
        result = {}
        #  
        if age_split < MINIMUM_MP_AGE:
            categ = "Under (or equal) {} years old".format(MINIMUM_MP_AGE)
            s = SetOfParliamentMember(categ)
            s.data_from_dataframe(data)
            result = {categ : s}
        #
        else:
            categ1 = "Under (or equal) {} years old".format(age_split)
            categ2 = "Over {} years old".format(age_split)
            s1, s2 = SetOfParliamentMember(categ1), SetOfParliamentMember(categ2)
            condition = data[AGE_YEARS_COLUMN_NAME] <= age_split
            data1 = data[condition]
            data2 = data[~condition]
            s1.data_from_dataframe(data1)
            s2.data_from_dataframe(data2)
            result = {
                categ1 : s1,
                categ2 : s2
            }
        #
        return result
    #    
    def __len__(self):
        return self.number_of_mps
    #
    #def __contains__(self, mp_name):
    #    return mp_name in self.dataframe["nom"].values
    #
    def __getitem__(self, index):
        try:
            result = dict(self.dataframe.ix[index])
        except:
            if index < 0:
                raise Exception("Please select a positive index")
            elif index >= len(self.dataframe):
                raise Exception("There are only {} MPs!".format(len(self.dataframe)))
            else:
                raise Exception("Wrong index")
        return result
    #
    @property
    def number_of_mps(self):
        return len(self.dataframe)

#    @number_of_mps.setter
#    def number_of_mps(self, value):
#        raise Exception("You can not set the number of MPs!")

    def __iter__(self):
        self.iterator_state = 0
        return self
    # 
    def __next__(self):
        if self.iterator_state >= len(self):
            raise StopIteration()
        result = self[self.iterator_state]
        self.iterator_state += 1
        return result

def launch_analysis(data_file, by_party=False, info=False, searchname=None) : 
    sopm = SetOfParliamentMembers('All MPs') # dans le tuto sopm
    sopm.data_from_csv(os.path.join('data/',data_file))
    if 1 == 0 : 
        sopm.display_chart()
    #
        if by_party : 
            for party, s in sopm.split_by_political_party().items(): 
                print(party,s)
                s.display_chart()
        if info:
            print(sopm.total_mps())
            print(sopm)
    if searchname != None : 
        print(searchname)
        is_present = searchname in sopm
        print(is_present)
        print("Testing if {} is present: {}".format(searchname, is_present)) # utilise contains 
#        print(searchname.__getitem__(searchname)) 
    # sopm.data_from_csv(os.path.join("data","current_mps.csv"))
    for mp in sopm:
        print(mp["nom"], mp["emails"])

if __name__ == "__main__":
    # main()
    launch_analysis('current_mps.csv')    

