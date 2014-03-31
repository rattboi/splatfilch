#!/usr/bin/env python
# pylint: disable-msg=C0103,C0326,C0111

import ConfigParser
import os.path
# import time
from datetime import datetime

class cSplatfilchConfig(object):
    filename =          '.splatfilch.cfg'
    lastrun_obj = None
    lastrun_fmt =      '%Y %m %d %H %M %S'

    def __init__(self):
        if not os.path.exists(self.filename):
            self.makeNew()

        config = ConfigParser.SafeConfigParser()
        config.read(self.filename)
        self.lastrun_obj = datetime.strptime(
            config.get('lastrun', 'datetime_str'), self.lastrun_fmt)

    def getLastrun(self, raw_str=False):
        if raw_str == False:
            return self.lastrun_obj
        else:
            return self.lastrun_obj.strftime(self.lastrun_fmt)

    def makeNew(self):
        config = ConfigParser.SafeConfigParser()
        config.add_section('lastrun')
        config.set('lastrun', 'datetime_str',
                datetime.today().strftime(self.lastrun_fmt))

        with open(self.filename, 'wb') as configfile:
            config.write(configfile)
