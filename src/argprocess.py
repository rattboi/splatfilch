#!/usr/bin/env python

import argparse

def get_args():
    # create the top-level parser
    parser = argparse.ArgumentParser(prog='splatfilch', 
        description='splatfilch can has options')
    parser.add_argument('-e', '--exit', action='store_true', help="don't show this message and exit")
    parser.add_argument('-v', '--verbosity', action='count', default=0,
        help="increase output verbosity")
    parser.add_argument('-s', '--stderr', action='store_true',
        help="print to stderr instead of logging to a file")

    sp = parser.add_subparsers()
    sp_update = sp.add_parser('update', help='Download new content since last run')
    sp_source = sp.add_parser('source', help='Manage {list,add,remove} %(prog)s sources')


    
    return parser.parse_args()

if __name__ == "__main__":
    args = get_args()
    print args.verbosity
