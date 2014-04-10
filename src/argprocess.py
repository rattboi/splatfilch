#!/usr/bin/env python

import argparse

def get_args():
    # create the top-level parser
    parser = argparse.ArgumentParser(prog='splatfilch', 
        description='splatfilch can has options')
    parser.add_argument('--verbosity', '-v', action='count',
        help="controls how much info is logged [supported: -v, -vv]")
    parser.add_argument('--stdout', '-s', action='store_true',
        help="print to stdout instead of logging to file")
    return parser.parse_args()
