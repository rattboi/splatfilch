#!/usr/bin/env python
# pylint: disable-msg=C0103,W0612

import urllib2

def internet_on():
    '''simple check to catch non-connectivity'''
    try:
        response = urllib2.urlopen('http://74.125.228.100', timeout=1)
        return True
    except urllib2.URLError as err:
        pass
    return False
