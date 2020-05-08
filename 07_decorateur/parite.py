#!/usr/bin/env python3 
#coding: utf-8 

import analysis.csv as c_an 
import analysis.xml as x_an 

import argparse

import logging as lg

def parse_arguments(): 
    parser = argparse.ArgumentParser() 
    parser.add_argument("-e","--extension",help="""Type of file to analyse. Is it a CSV or a XML file?""")
    parser.add_argument("-i","--info",action='store_true',help="""Give the number of deputy.""")
    parser.add_argument("-p","--byparty",action='store_true',help="displays a graph for each political party")
    parser.add_argument("-s","--searchname",help="search a political by him name")
    parser.add_argument("-d","--index",help="search a political by an index")
    parser.add_argument("-g","--groupfirst",help="print the n political biggest groups")


    parser.add_argument("-v", "--verbose", action='store_true', help="""Make the application talk!""")
    return parser.parse_args()

def main(): 
    args = parse_arguments()
    if args.verbose:
        lg.basicConfig(level=lg.DEBUG) # enable the debugging level
    try : 
        if args.extension == 'csv': 
            c_an.launch_analysis('current_mps.csv', args.byparty,args.info,args.searchname)
        elif args.extension =='xml': 
            x_an.launch_analysis('SyceronBrut.xml')
    except FileNotFoundError as e: 
                print("File not found :", e)
#       lg.warning('Aaaa')
    finally:
                lg.info('#################### Analysis is over ######################')    

if __name__ == "__main__":
    main() 
