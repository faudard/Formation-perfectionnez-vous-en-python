#!/usr/bin/env python3 
#coding: utf-8 

import os 


def launch_analysis(data_file):
    directory = os.path.dirname(os.path.dirname(__file__))
    path_to_file = os.path.join(directory, "data", data_file)
    print('we load this file path ', path_to_file)

#def main():
#    path_to_file='data/'
    with open(path_to_file,'r') as file:
        preview = file.readline()

    # Clean file
    pp = preview.split(';')
    pp2 = [x.replace('\n', '') for x in pp] 
    print('Here is a preview: {}'.format(pp2)) 

    # we can also use pandas 
#    import pandas as pd 
#    pp3 = pd.csv_read(path_to_file)
#    print(pp3.keys())

if __name__ == "__main__":
    # main()
    launch_analysis('SyceronBrut.xml')    

