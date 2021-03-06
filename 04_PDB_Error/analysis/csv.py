#!/usr/bin/env python3 
#coding: utf-8 

import os 
import logging as lg

#lg.basicConfig(level=lg.DEBUG) # enable the debugging level

def launch_analysis(data_file):
    directory = os.path.dirname(os.path.dirname(__file__)) 
    path_to_file = os.path.join(directory, "data", data_file)
#    print('we load this file path ', path_to_file)

#def main():
#    path_to_file='data/'
    try:
        with open(path_to_file,'r') as file:
            preview = file.readline()
        pp = preview.split(';')
        pp2 = [x.replace('\n', '') for x in pp] 
        lg.debug('Here is a preview: {}'.format(pp2)) 

    except IOError as e: 
        lg.critical("File not found! {}".format(e))
    # Clean file

    # we can also use pandas 
#    import pandas as pd 
#    pp3 = pd.csv_read(path_to_file)
#    print(pp3.keys())

if __name__ == "__main__":
    # main()
    launch_analysis('current_mps.csv')    

