#!/usr/bin/env python

import argparse

def get_args():
    # create the top-level parser
    parser = argparse.ArgumentParser(prog='splatfilch', 
        description='splatfilch has two modes of operation.  additional help is\
        available for each mode with the -h flag')
    subparsers = parser.add_subparsers(help='Selects between operating modes')

    # create the parser for the "command_1" command
    single_parser = subparsers.add_parser('SINGLE', 
        description='Single mode allows detailed filching of a single tag', 
        help='Single mode allows detailed filching of a single tag')
    single_parser.add_argument('a', type=str, help='test arg for single mode arg a')

    # create the parser for the "command_2" command
    batch_parser = subparsers.add_parser('BATCH', 
        description='Batch mode allows automated filching of multiple tags', 
        help='Batch mode allows automated filching of multiple tags')
    batch_parser.add_argument('b', type=str, help='test arg for batch mode arg b')
    batch_parser.add_argument('-c', type=str, help='test arg for batch mode arg c')

    return parser.parse_args()