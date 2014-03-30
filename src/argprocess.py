#!/usr/bin/env python

import argparse

def get_args():
    # create the top-level parser
    parser = argparse.ArgumentParser(prog='splatfilch', 
        description='splatfilch can has options')
    return parser.parse_args()
