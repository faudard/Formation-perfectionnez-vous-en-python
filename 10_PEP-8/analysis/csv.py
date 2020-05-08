#!/usr/bin/env python3
#coding: utf-8
"""
Read csv and analysis
"""
import os
import datetime as dt

#import logging as lg
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
#import seaborn as sns

AGE_COLUMN_NAME = "age"                 # Name of the new column (containing the age of the MP)
                                        # to create in the dataframe
AGE_YEARS_COLUMN_NAME = "age_in_years"
BIRTH_COLUMN_NAME = "birth"

MINIMUM_MP_AGE = 18


class SetOfParliamentMembers:
    """
    set of parliament members
    """
    ALL_REGISTERED_PARTIES = [] # This is a class attribute
    def __init__(self, name):
        self.name = name
    #
    def data_from_csv(self, csv_file):
        """
        get data from csv file
        """
        self.dataframe = pd.read_csv(csv_file, sep=";")
    # On peut supprimer la fonction suivant mais j ai gardé pour la forme
    #
    def data_from_dataframe(self, dataframe):
        """
        data from dataframe
        """
        self.dataframe = dataframe
    #
    #
    def display_chart(self):
        """
        display chart
        """
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
        labels = ["Female ({})".format(
            counts[0]), "Male ({})".format(counts[1])]
        fig, axis = plt.subplots()
        axis.axis("equal")
        axis.pie(proportions, labels=labels, autopct="%1.1f pourcents")
        plt.title("{} ({} MPs)".format(self.name, nb_mps))
        plt.show()
    #
    @staticmethod
    def display_histogram(values):
        """
        display histo
        """
        fig, axis = plt.subplots()
        axis.hist(values, bins=20)
        plt.title("Ages ({} MPs)".format(len(values)))
        plt.show()
    #
    def split_by_political_party(self):
        """
        split by policial party
        """
        result = {}
        data = self.dataframe
        #
        all_parties = data["parti_ratt_financier"].dropna().unique()
        # dropna supprime les NaN unique les doublons
        #
        for party in all_parties:
            data_subset = data[data.parti_ratt_financier == party]
            subset = SetOfParliamentMembers(
                'MPS from party "{}"'.format(party))
            subset.data_from_dataframe(data_subset)
            result[party] = subset
        #
        return result
    #
    def _compute_age_column(self):
        now = dt.datetime.now()
        data = self.dataframe
        #
        # In data, the column "date_naissance"  still
        #contains string (ex:"1945-08-10")
        # We first have to convert this to a column of type datetime.
        if not BIRTH_COLUMN_NAME in data.columns:
            data[BIRTH_COLUMN_NAME] = \
                data["date_naissance"].apply(
                    lambda string: dt.datetime.strptime(
                        string, "%Y-%m-%d"))

        if not AGE_COLUMN_NAME in data.columns:
            data[AGE_COLUMN_NAME] = data[BIRTH_COLUMN_NAME].apply(
                lambda date: now-date)

        # Here is an other way to fill a column of a
        #dataframe (less elegant than the previous ones!):
        new_column = []
        for age in data[AGE_COLUMN_NAME]:
            # age is of type datetime.timedelta (because it was
            # calculated from a difference between two dates)
            # Here, we want to convert it to an integer containing
            # the the age, expressed in years.
            age_in_years = int(age.days / 365)
            new_column += [age_in_years]
        data[AGE_YEARS_COLUMN_NAME] = new_column
    #
    def split_by_age(self, age_split):
        """
        split by age
        """
        data = self.dataframe
        self._compute_age_column()
        self.display_histogram(data[AGE_YEARS_COLUMN_NAME].values)
        #
        result = {}
        #
        if age_split < MINIMUM_MP_AGE:
            categ = "Under (or equal) {} years old".format(
                MINIMUM_MP_AGE)
            s = SetOfParliamentMembers(categ)
            s.data_from_dataframe(data)
            result = {categ : s}
        #
        else:
            categ1 = "Under (or equal) {} years old".format(age_split)
            categ2 = "Over {} years old".format(age_split)
            s1, s2 = SetOfParliamentMembers(categ1), SetOfParliamentMembers(categ2)
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
    #
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


def launch_analysis(data_file, by_party=False,
                    info=False, searchname=None):
    sopm = SetOfParliamentMembers('All MPs') # dans le tuto sopm
    sopm.data_from_csv(os.path.join('data/', data_file))
    if 1 == 0:
        sopm.display_chart()
    #
        if by_party:
            for party, s1 in sopm.split_by_political_party().items():
                print(party, s1)
                s1.display_chart()
        if info:
            #print(sopm.total_mps())
            print(sopm)
    if searchname is not None:
        print(searchname)
        is_present = searchname in sopm
        print(is_present)
        print("Testing if {} is present: {}".format(
            searchname, is_present)) # utilise contains
#        print(searchname.__getitem__(searchname))
    # sopm.data_from_csv(os.path.join("data","current_mps.csv"))
    for mp2 in sopm:
        print(mp2["nom"], mp2["emails"])

if __name__ == "__main__":
    launch_analysis('current_mps.csv')
