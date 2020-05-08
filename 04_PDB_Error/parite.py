#!/usr/bin/env python3 
#coding: utf-8 

# Old 
#import csv_analysis as c_an
#import xml_analysis as x_an 

import analysis.csv as c_an 
import analysis.xml as x_an 

import argparse

import logging as lg

def parse_arguments(): 
    parser = argparse.ArgumentParser() 
    parser.add_argument("-e","--extension",help="""Type of file to analyse. Is it a CSV or a XML file?""") 
    parser.add_argument("-v", "--verbose", action='store_true', help="""Make the application talk!""")
    return parser.parse_args()

def main(): 
    args = parse_arguments()
    if args.verbose:
        lg.basicConfig(level=lg.DEBUG) # enable the debugging level
# 4-- Add debugging 
#    import pdb ;pdb.set_trace()

# 4-- Sample example for try 
#    try :
#        0/"la tete a toto"
#    except TypeError as 0:
#        print("0 divided by a string it's impossible!") 


    #print(args.extension)
    try : 
        if args.extension == 'csv': 
            c_an.launch_analysis('current_mps.csv')
        elif args.extension =='xml': 
            x_an.launch_analysis('SyceronBrut.xml')
    except FileNotFoundError as e: 
                print("File not found :", e)
#       lg.warning('Aaaa')
    finally:
                lg.info('#################### Analysis is over ######################')    

if __name__ == "__main__":
    main() 
