#!/usr/bin/env python
# pylint: disable-msg=R0903,C0111

import logging

class CTextCache(object):
    '''very basic cache file. see isInCache(item) for functionality'''
    cache_filename = ".cache.splatfilch"
    cached_items = []
    cache_size = 512

    def __init__(self):
        '''reads cachefile into queue'''
        
        self.logger = logging.getLogger('cache')

        try:
            with open(self.cache_filename, 'r') as infile:
                self.cached_items = [line.strip() for line in infile]
                self.logger.info("opening cache file")
        except IOError:
            self.logger.warning("no cache file found. created new cache file")

    def __del__(self):
        with open(self.cache_filename, 'w+') as output:
            for entry in self.cached_items:
                output.write("%s\n" % entry)

    def already_in_cache(self, item):
        ''' if in cache, does nothing and returns true \
            if not in cache, adds to cache and returns false'''
        if item in self.cached_items:
            return True     # item was already in cache (still is)

        else:
            # pop an item from the cache if it is full
            if len(self.cached_items) >= self.cache_size:
                self.cached_items.pop(0)

            # add the current item to the cache
            self.cached_items.append(item)
            return False    # item was not in cache (but now it is)

    def remove_from_cache(self, item):
        ''' if in cache, removes item and returns false.  if not in cache \
                returns true'''
        if item in self.cached_items:
            self.cached_items.remove(item)
            return False
        else:
            return True

