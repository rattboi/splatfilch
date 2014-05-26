#!/usr/bin/env python
'''
a simple list-based cache which is little more than a specialized FIFO.  the
main method, lookup() handles the majority of the functionality of the class,
however an explicit resize() method is provided for convenience.

usage:
>>> c = CacheList('temp', 2)

# the first lookup should return false, but place 'first' in the cache
>>> c.lookup("first")
False
>>> print c.cache
['first']

# now attempting to lookup first should return true since it is in the cache
>>> c.lookup("first")
True

# add 'second' (should return false) and view the cache to confirm it was added
>>> c.lookup("second")
False
>>> print c.cache
['second', 'first']

# since cache size is 2, adding a third item should push 'first' out
>>> c.lookup("third")
False
>>> print c.cache
['third', 'second']

# attempting to lookup 'first' in this state will re-add it to the cache.
>>> c.lookup("first")
False
>>> print c.cache
['first', 'third']
    '''

import logging

class CacheList(object):
    ''' a simple cache implemented with a fifo'''

    def __init__(self, path, max_size):
        '''attempts to return a list generated from the file specified.  only
        the  max_size newest items read from the file are kept

        if the file cannot be found or read, a new file is created and a blank
        list is returned.'''

        self.logger = logging.getLogger('cache')
        self.max_size = max_size
        self.path = path

        try:
            with open(path, 'r') as infile:
                self.cache = [line.strip() for line in infile]
                self.logger.info("successfully opened cachefile")
                self.resize(max_size)

        except IOError:
            self.cache = []
            self.logger.warning("no cachefile found, created new cachefile")

    def __del__(self):
        with open(self.path, 'w+') as output:
            for entry in self.cache:
                output.write("%s\n" % entry)
        self.logger.info("cachefile written to disk")

    def lookup(self, item):
        ''' if in cache, does nothing and returns true \
            if not in cache, adds to cache and returns false'''

        if item in self.cache:
            self.logger.warning("'%s' is already in the cache" % item)
            return True

        else:
            # pop an item from the cache if it is full
            self.cache = self.cache[:self.max_size - 1]
            self.cache.insert(0, item)
            self.logger.info("'%s' was not present.  added to cache" % item)
            return False    # item was not in cache (but now it is)

    def resize(self, new_size):
        '''manual resize, provided for conveinence'''

        if len(self.cache) > new_size:
            self.cache = self.cache[:new_size]
            self.max_size = new_size
            self.logger.info("cache resized to hold up to %d items" % new_size)

if __name__ == "__main__":
    import doctest
    import os
    if os.path.exists('temp'):
        os.remove('temp')

    logging.basicConfig(level=20)
    doctest.testmod()

    if os.path.exists('temp'):
        os.remove('temp')
