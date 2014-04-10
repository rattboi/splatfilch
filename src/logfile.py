#!/usr/bin/env python

from datetime import datetime
import os
import sys

# establish verbosity levels:
QUIET, VERBOSE, DEBUG = range(3)

class LogFile(object):
    log_directory = "./log"
    filename_base = log_directory + "/splatfilch_"
    start_time = datetime.today()
    wr_target = None
    verbosity = QUIET

    def __init__(self, args):
        '''begins a new logfile with the current date/time'''

        # set the verbosity level
        if args.verbosity == None:
            self.verbosity = QUIET
        else:
            self.verbosity = args.verbosity

        # make the directory if it does not exist
        if not os.path.isdir(self.log_directory):
            os.makedirs(self.log_directory)

        # put today's date and time on the log file
        filename = self.filename_base + \
            self.start_time.strftime('%Y%m%d_%H%M%S')

        # append extension
        filename += ".txt"

        self.wr_target = sys.stdout if args.stdout else open(filename, 'w')
        self.wr_target.write(self.start_time.strftime(
            "=== Splatfilch runtime log for %m-%d-%Y, %I:%M:%S %p ===\n"))

    def __del__(self):
        if self.wr_target is not sys.stdout:
            self.wr_target.close()

    def error(self, msg):
        '''always writes to log file.  use for unrecoverable/fatal errors'''
        self.wr_target.write("<  ERROR  >  " + msg + "\n")

    def warning(self, msg):
        '''writes to log file when verbosity is enabled.  use for warnings \
        regarding uncertain results or strange behavior that is not fatal.'''
        if self.verbosity >= VERBOSE:
            self.wr_target.write("< WARNING >  " + msg + "\n")

    def info(self, msg):
        '''only writes to log file if debug verbosity is enabled.  no message \
        is too mundane for this logging level as it may not even be exposed \
        to the user.'''
        if self.verbosity >= DEBUG:
            self.wr_target.write("<  DEBUG  >  " + msg + "\n")
