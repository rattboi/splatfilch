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
from datetime import datetime
import logging
import sys

### SPLATFILCH LIBRARY IMPORTS
from argparser_init import splatfilch_argparser
from source_manager import addchannel_ui, rmchannel_ui, lschannel_ui
from json_config import config_read, config_write
from cachefile import CTextCache
from connection_test import internet_on
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

######################### PREPROCESSING #############################
# process the command line arguments
ARGS = splatfilch_argparser().parse_args()

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
CONFIG = config_read(CONFIGNAME)

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

    config_write(CONFIG, CONFIGNAME)
    exit()


# UPDATE MODE
# ----------------------
# the normal mode of operation for the program.
# iterates through all sources, downloads/converts new uploads from each.

# read splatfilch config to find last run time/date, get output dirs
if CONFIG['lastrun'] == "":
    LAST_RUN = datetime.now()
    CONFIG['lastrun'] = LAST_RUN.strftime(DATETIME_FMT)
else:
    LAST_RUN = datetime.strptime(CONFIG['lastrun'], DATETIME_FMT)

LOG.info("last run was " + CONFIG['lastrun'])

# read cache, and other program settings
CACHE = CTextCache()

# (future) open the previous log file respond to previous errors

# basic test to establish connectivity
if not internet_on():
    LOG.error("no can has interwebs.  please check your internet connection")
    exit(-1)

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
config_write(CONFIG, CONFIGNAME)

exit(0)
