#!/usr/bin/env python3 
#coding: utf-8 

# Old 
#import csv_analysis as c_an
#import xml_analysis as x_an 

import analysis.csv as c_an 
import analysis.xml as x_an 

import argparse


def parse_arguments(): 
    parser = argparse.ArgumentParser() 
    parser.add_argument("-e","--extension",help="""Type of file to analyse. Is it a CSV or a XML file?""") 
    return parser.parse_args()

def main(): 
    args = parse_arguments()
    #print(args.extension)
    if args.extension == 'csv': 
        c_an.launch_analysis('current_mps.csv')
    elif args.extension =='xml': 
        x_an.launch_analysis('SyceronBrut.xml')
    #else : 
    #    raise('no format given!') 


if __name__ == "__main__":
    main() 
