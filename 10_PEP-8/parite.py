#!/usr/bin/env python3
#coding: utf-8
"""
============================================
  Analyse Woman / Man balance in Politics
============================================
"""
import argparse

import logging as lg

import re

import analysis.csv as c_an
import analysis.xml as x_an

def parse_arguments():
    """
    Parse arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--extension",
                        help="""Type of file to analyse. Is it a CSV or a XML file?""")
    parser.add_argument("-d", "--datafile",
                        help="""CSV file containing pieces of
        information about the members of parliament""")
    parser.add_argument("-i", "--info", action='store_true',
                        help="""Give the number of deputy.""")
    parser.add_argument("-p", "--byparty", action='store_true',
                        help="displays a graph for each political party")
    parser.add_argument("-s", "--searchname",
                        help="search a political by him name")
    parser.add_argument("-I", "--index",
                        help="search a political by an index")
    parser.add_argument("-g", "--groupfirst",
                        help="print the n political biggest groups")
    parser.add_argument("-v", "--verbose", action='store_true',
                        help="""Make the application talk!""")
    return parser.parse_args()

def main():
    """
    Main
    """
    args = parse_arguments()
    datafile = args.datafile
    if args.verbose:
        lg.basicConfig(level=lg.DEBUG) # enable the debugging level
    try:
        ext = re.search(r'^.+\.(\D{3})$', args.datafile)
        extension = ext.group(1)
        print(extension)
        if extension == 'csv':
            c_an.launch_analysis(datafile, args.byparty, args.info, args.searchname)
        elif extension == 'xml':
            x_an.launch_analysis(datafile)
    except FileNotFoundError as err:
        print("File not found :", err)
#       lg.warning('Aaaa')
    finally:
        lg.info('#################### Analysis is over ######################')

if __name__ == "__main__":
    main()
