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
            self.cache_data.pop(self.last_item)
            print('DISCARD:', self.last_item)
        if key:
            self.last_item = key

    def get(self, key):
        """returns value of item linked to key"""
        return self.cache_data.get(key)
