#!/usr/bin/env python3
"""
LIFO Caching
"""


from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ Class LIFOCache that inherits from BaseCaching """

    def __init__(self):
        """ Funtion that overload superclass init """
        super().__init__()
        self.datakeys = []

    def put(self, key, item):
        """ Function that assigns the value of the element
        in dictionary """
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS and \
                key not in self.datakeys:
            discard = self.datakeys.pop()
            del self.cache_data[discard]
            print('DISCARD: {}'.format(discard))

        if key and item:
            self.datakeys.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ Function that return the value of dictionary """
        if key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
