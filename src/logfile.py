#!/usr/bin/env python

from datetime import datetime
import os

# establish error levels:
DBG, WARN, ERR = range(3)

class LogFile(object):
    log_directory = "./log"
    filename_base = log_directory + "/splatfilch_"
    start_time = datetime.today()

    def __init__(self):
        '''begins a new logfile with the current date/time'''

        # make the directory if it does not exist
        if not os.path.isdir(self.log_directory):
            os.makedirs(self.log_directory)

        # put today's date and time on the log file
        filename = self.filename_base + \
                self.start_time.strftime('%Y%m%d_%H%M%S')

        # append extension
        filename += ".txt"

        with open(filename, 'w') as fptr:
            fptr.write(self.start_time.strftime(
                "=== Splatfilch runtime log for %m-%d-%Y, %I:%M:%S %p ===\n"))

log = LogFile()

