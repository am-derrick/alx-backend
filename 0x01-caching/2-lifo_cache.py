#!/usr/bin/env python3
"""LIFO caching"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO caching sytem"""
    def __init__(self):
        """initialises the class instance"""
        super().__init__()

    def put(self, key, item):
        """adds item value corresponding to key"""
        if key and item:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            key_discarded = sort(self.cache_data)[-1]
            self.cache_data.pop(key_discarded)
            print('DISCARD: {}'.format(key_discarded))

    def get(self, key):
        """returns value of item linked to key"""
        return self.cache_data.get(key)
