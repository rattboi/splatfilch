#!/usr/bin/env python
# pylint: disable-msg=C0103,C0326,R0903,C0111

class cTextCache(object):
    '''very basic cache file. see isInCache(item) for functionality'''
    cache_filename  = ".splatfilch.cachefile"
    cached_items    = []
    __cache_size__  = 512

    def __init__(self):
        '''reads cachefile into queue'''
        try:
            with open(self.cache_filename, 'r') as infile:
                self.cached_items = [line.strip() for line in infile]
        except IOError:
            pass

    def __del__(self):
        with open(self.cache_filename, 'w+') as output:
            for entry in self.cached_items:
                output.write("%s\n" % entry)

    def AlreadyInCache(self, item):
        ''' if in cache, does nothing and returns true \
            if not in cache, adds to cache and returns false'''
        if item in self.cached_items:
            return True     # item was already in cache (still is)

        else:
            # pop an item from the cache if it is full
            if len(self.cached_items) >= self.__cache_size__:
                self.cached_items.pop(0)

            # add the current item to the cache
            self.cached_items.append(item)
            return False    # item was not in cache (but now it is)
