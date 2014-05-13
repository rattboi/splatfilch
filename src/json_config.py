#!/usr/bin/env python
''' methods for simplifying the (already simple) management of settings json'''

import json
import os.path

BLANKFILE = {'lastrun'   : "",
             'output_dir': "./downloads",
             'channels'  : {}
            }

def config_read(filename):
    if os.path.isfile(filename):
        with open(filename, 'r') as infile:
            return json.load(infile)
    else:
        return BLANKFILE

def config_write(config_dict, filename):
    with open(filename, 'w') as outfile:
        json.dump(config_dict, outfile, indent=4)

if __name__ == "__main__":

    TEST_FILE = "test.json"
    if os.path.isfile(TEST_FILE):
        print "file exists"
    else:
        print TEST_FILE + " not found, creating new"

    CONFIG = config_read(TEST_FILE)
    config_write(TEST_FILE, CONFIG)

    with open(TEST_FILE, 'r') as readback:
        CONFIG = json.load(readback)

    print json.dumps(CONFIG, indent=2)
