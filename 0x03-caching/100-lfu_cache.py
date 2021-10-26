#!/usr/bin/python3
""" LFU Dictionary """


from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ class LFUCache that inherits from BaseCaching """

    def __init__(self):
        """ Funtion that overload superclass init """
        super().__init__()
        self.datakeys = []
        self.count = {}

    def put(self, key, item):
        """ Function that assigns the value of the element
        in dictionary """
        if not key or not item:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS and \
                key not in self.datakeys:
            self.discard()
        if key not in self.cache_data:
            self.count[key] = 1
        else:
            self.count[key] += 1
            self.datakeys.remove(key)
        self.datakeys.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """ Function that return the value of dictionary """
        if key in self.cache_data:
            self.count[key] += 1
            self.datakeys.remove(key)
            self.datakeys.append(key)
            return self.cache_data[key]
        else:
            return None

    def discard(self):
        """ discard item and print"""
        m_time = min(self.count.values())
        keys = [k for k, v in self.count.items() if v == m_time]
        low = 0
        while self.datakeys[low] not in keys:
            low += 1
        discard = self.datakeys.pop(low)
        del self.cache_data[discard]
        del self.count[discard]
        print('DISCARD: {}'.format(discard))
