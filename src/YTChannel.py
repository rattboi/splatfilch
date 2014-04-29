#!/usr/bin/env python

class YTChannel(object):
    
    def __init__(self, user_name, id3_regex = "(.+?)( - )(.*)"):
        self.user_name = user_name
        self.id3_regex = id3_regex
        
    
    user_name = None
    id3_regex = None
    display_name = None

