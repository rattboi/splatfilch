#!/usr/bin/env python
#####################################################################
# file:     Splatfilch.py
# authors:  Eric Krause
#           Erik Rhodes
# 
# descr:    top-level file for splatfilch program.  features marked
#           as (future) are beyond the scope of milestone 1
#####################################################################

### PYLINT OPTIONS
# pylint: disable-msg=C0103

### IMPORTS
import argprocess

### GLOBAL CONSTANTS
# currently none

######################### PREPROCESSING #############################

# process command line options and respond as needed
args = argprocess.get_args()

# read splatfilch config to find last run time/date, get output dirs
#   read cache, and other program settings

# (future) open the previous log file respond to previous errors

# (future) create logfile for current run

# basic test to establish connectivity


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

exit(0)
