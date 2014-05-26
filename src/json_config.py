#!/usr/bin/env python
''' methods for simplifying the (already simple) management of settings json'''
# pylint: disable=bad-whitespace

import json
import os.path
import logging
from datetime import datetime

logger = logging.getLogger('json_config')

DATETIME_FMT = "%Y-%m-%d %H:%M:%S"      # date/time format used in config file

BLANKFILE = { 'general'  : { 'lastrun' : datetime.now().strftime(DATETIME_FMT),
                             'downloads' : './downloads'
                           },

              'cache'    : { 'path' : './.cache.txt',
                             'max_size' : 1024
                           },

              'channels' : {}
            }

def config_read(filename):
    if os.path.isfile(filename):
        logger.info("successfully opened config file")
        with open(filename, 'r') as infile:
            return json.load(infile)
    else:
        logger.warning("no config found, created new file from defaults")
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
