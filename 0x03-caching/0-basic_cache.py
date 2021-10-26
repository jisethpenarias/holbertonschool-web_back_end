#!/usr/bin/env python3
"""
Create Basic dictionary a class BasicCache that inherits from BaseCaching
"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ Create a class BasicCache that inherits from BaseCaching """

    def put(self, key, item):
        """ Function that assigns the value of the element
        to the dictionary self.cache_data """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Function that return the value of dictionary """
        if key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
