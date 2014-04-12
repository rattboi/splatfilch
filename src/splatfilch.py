#!/usr/bin/env python
#####################################################################
# file:     Splatfilch.py
# authors:  Eric Krause
#           Erik Rhodes
# descr:    top-level file for splatfilch program.  features marked
#           as (future) are beyond the scope of milestone 1
#####################################################################

### PYLINT OPTIONS
# pylint: disable-msg=C0103

### STL IMPORTS
from datetime import datetime
import logging

### SPLATFILCH LIBRARY IMPORTS
from argprocess import get_args
from configmanagement import cSplatfilchConfig
from cachefile import CTextCache
from connection_test import internet_on

### GLOBAL CONSTANTS
log = None          # will be the logfile object after arg parsing
LOG_LVLS = {
    #   logging.CRITICAL # major error. sw may not be able to keep running
    0 : logging.ERROR,   # serous problem. sw cannot perform some function
    1 : logging.WARNING, # an unexpected situation. or problem in near future
    2 : logging.INFO     # confirmation things are working as expected
    #   logging.DEBUG    # detailed info, only of intrest for diagnosing bugs
}

######################### PREPROCESSING #############################

# process command line options and respond as needed
args = get_args()

#  create logfile for current run
logger = logging.getLogger()
logger.setLevel(LOG_LVLS[args.verbosity] if args.verbosity < 3 else 2)
formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')

if (args.stdout):
    # create console handler and set level to info
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
else:
    # create error file handler and set level to error
    filename=datetime.today().strftime("./log/splatfilch_%Y%m%d_%H%M%S.txt")
    handler = logging.FileHandler(filename)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

logger.debug('All systems operational')
logger.info('Airspeed 300 knots')
logger.warn('Low on fuel')
logger.error('No fuel. Trying to glide.')
logger.critical('Glide attempt failed. About to crash.')

# read splatfilch config to find last run time/date, get output dirs
cfg = cSplatfilchConfig()   # create config handler obj
lastrun = cfg.getLastrun()  # lastrun is a datetime obj

# read cache, and other program settings
CACHE = CTextCache()

# (future) open the previous log file respond to previous errors

# basic test to establish connectivity
if not internet_on():
    log.error("no can has interwebs.  please check your internet connection")
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
cfg.setLastrun(datetime.now())

exit(0)
