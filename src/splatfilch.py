#!/usr/bin/env python
#####################################################################
# file:     Splatfilch.py
# authors:  Eric Krause
#           Erik Rhodes
# descr:    top-level file for splatfilch program.  features marked
#           as (future) are beyond the scope of milestone 1
#####################################################################

### PYLINT OPTIONS
# pylint: disable-msg=

### STL IMPORTS
from datetime import datetime, timedelta
import os
import logging
import sys
import urllib2

### SPLATFILCH LIBRARY IMPORTS
import json_config
from argparser_init import splatfilch_argparser
from source_manager import addchannel_ui, rmchannel_ui, lschannel_ui
from cachefile import CTextCache
from rfc3339 import rfc3339

### GLOBAL CONSTANTS
CONFIGNAME = "config_splatfilch.json"   # name of config file
DATETIME_FMT = "%Y-%m-%d %H:%M:%S"      # date/time format used in config file
LAST_RUN = None                         # last run date and time (datetime obj)
LOG_LVLS = {
    #   logging.CRITICAL # major error. sw may not be able to keep running
    0 : logging.ERROR,   # serous problem. sw cannot perform some function
    1 : logging.WARNING, # an unexpected situation. or problem in near future
    2 : logging.INFO     # confirmation things are working as expected
    #   logging.DEBUG    # detailed info, only of intrest for diagnosing bugs
}

# PREPROCESSING
# ----------------------
# parse arguments, set up the logger, and read in the config file
ARGS = splatfilch_argparser().parse_args()

# create log directory if it does not exist
if not os.path.exists('log'):
    os.makedirs('log')

# set up logger
logging.basicConfig(
    level=LOG_LVLS[ARGS.verbosity] if ARGS.verbosity < 3 else 2,
    format='%(asctime)s.%(msecs).3s %(name)-12s %(levelname)-8s %(message)s',
    datefmt='%T',
    filename=None if ARGS.stderr else datetime.today()
        .strftime("./log/splatfilch_%Y-%m-%d__%H-%M-%S.txt"),
    filemode='w',
    stream=sys.stderr if ARGS.stderr else None
)
LOG = logging.getLogger('main')
LOG.info('logger configured')

# read in config file
CONFIG = json_config.config_read(CONFIGNAME)

# SOURCE MANAGEMENT MODE
# ----------------------
# a simple auxilary operation mode for adding/removing/listing sources
if ARGS.mode == 'source':
    if ARGS.source_mode == 'list':
        lschannel_ui(CONFIG)

    elif ARGS.source_mode == 'search':
        new_channel = addchannel_ui(ARGS.search_term)
        if new_channel != None:
            CONFIG['channels'][new_channel.title] = new_channel.id

    elif ARGS.source_mode == 'remove':
        rm_channel = rmchannel_ui(CONFIG, ARGS.channel)
        if rm_channel != None:
            del CONFIG['channels'][rm_channel]

    json_config.config_write(CONFIG, CONFIGNAME)
    exit()


# UPDATE MODE
# ----------------------
# the normal mode of operation for the program.
# iterates through all sources, downloads/converts new uploads from each.

# basic test to establish connectivity
try:
    urllib2.urlopen('http://74.125.228.100', timeout=1)
    LOG.info("internet connectivity seems OK")
except urllib2.URLError as err:
    LOG.error("no internet connectivity.  check your internet connection")
    exit(-1)

# open the cachefile
CACHE = CTextCache()

# read splatfilch config to find last run time/date, get output dirs
LAST_RUN = datetime.strptime(CONFIG['lastrun'], json_config.DATETIME_FMT)

# if last run was less than X time ago, don't run again.
if LAST_RUN > (datetime.today() - timedelta(seconds=5)):
    LOG.error("last run was like 5 seconds ago.  calm down.")
    exit(-1)
else:
    LOG.info("last run was " + CONFIG['lastrun'])

# (future) open the previous log file respond to previous errors


###################### ACCUMULATION PHASE ###########################

# determine channel(s) to scrape (will be hardcoded in milestone 1)

# get recent uploads from channel (newer than last run date)

# perform duplicate detection
#   - extract artist, track from vid title (gdata or vid page regex)
#   - (future) fuzzy compare against cache of recent downloads
#   - straight compare against recent d/l cache for exact duplicates

# for each new and unique video, add it to the 'to download' list
#   - note: might be good to include title-artist-channel in same
#           list, so that this info does not need to be re-extracted


######################## DOWNLOAD PHASE #############################

# process every entry in the 'to-download' list
#   - download the video with correct youtube-dl settings
#       - note: modify youtube-dl --output flag per download so files
#               have correct names when initially downloaded
#   - flag failures/unusual things in log file
#   - (future) set id3 tags of file
#   - move file to correct location if applicable


######################## CLEANUP PHASE ##############################

# close out log file (maybe rename it to indicate errors/no errors?)

# send notifications to users based on files SUCCESSFULLY downloaded

# update lastrun date/time
CONFIG['lastrun'] = datetime.today().strftime(DATETIME_FMT)
LOG.info("last run set to: " + CONFIG['lastrun'])
json_config.config_write(CONFIG, CONFIGNAME)

exit(0)
