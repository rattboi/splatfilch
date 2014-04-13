#!/usr/bin/env python

import argparse

def get_args():
    # create the top-level parser
    parser = argparse.ArgumentParser(prog='splatfilch', 
        description='splatfilch can has options')
    parser.add_argument('--verbosity', '-v', action='count', default=0,
        help="controls how much info is logged [supported: -v, -vv]")
    parser.add_argument('--stderr', '-s', action='store_true',
        help="print to stderr instead of logging to file")
    return parser.parse_args()
