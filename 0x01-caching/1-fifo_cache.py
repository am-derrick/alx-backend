#!/usr/bin/env python3
"""FIFO caching"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFO Caching System"""
    def __init__(self):
        """initializes the class instance"""
        super().__init__()

    def put(self, key, item):
        """adds item in cache"""
        if key and item:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            key_discarded = sorted(self.cache_data)[0]
            self.cache_data.pop(key_discarded)
            print('DISCARD: {}'.format(key_discarded))

    def get(self, key):
        """Gets an item using key"""
        return self.cache_data.get(key)
