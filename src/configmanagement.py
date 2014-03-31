#!/usr/bin/env python
# pylint: disable-msg=C0103,C0326

import ConfigParser
import os.path
# import time
from datetime import datetime

class cSplatfilchConfig(object):
    ''' wrapper around ConfigParser, specialized for splatfilch'''
    filename =          '.splatfilch.cfg'
    lastrun_obj = None
    lastrun_fmt =      '%Y %m %d %H %M %S'
    config = ConfigParser.SafeConfigParser()

    def __init__(self):
        ''' ctor populates members, uses defaults if no cfg file'''
        # create the file if not present
        if not os.path.exists(self.filename):
            #add default sections and set to today
            self.config.add_section('lastrun')
            self.setLastrun(datetime.today())

        # else file exists: read out options and set class members
        self.config = ConfigParser.SafeConfigParser()
        self.config.read(self.filename)
        # decode formatted string back into datetime obj
        self.lastrun_obj = datetime.strptime(
            self.config.get('lastrun', 'datetime_str'), self.lastrun_fmt)

    def __del__(self):
        ''' ctor writes all changed options to cfg file'''
        with open(self.filename, 'wb') as configfile:
            self.config.write(configfile)

    def getLastrun(self):
        ''' no formatting applied to datetime obj returned'''
        return self.lastrun_obj

    def setLastrun(self, datetime_obj):
        ''' set lastrun in config file using datetime obj'''
        self.config.set('lastrun', 'datetime_str',
            datetime_obj.strftime(self.lastrun_fmt))
