#!/usr/bin/env python3
"""LFU Caching"""
from base_caching import BaseCaching
from collections import OrderedDict


class LFUCache(BaseCaching):
    """LFU Caching System"""
    def __init__(self):
        """initialises the class instance"""
        super().__init__()
        self.cache_data = OrderedDict()
        self.mru = ""

    def put(self, key, item):
        """adds item in cache"""
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if key in self.cache_data:
                    self.cache_data.updat({key: item})
                    self.mru
                else:
                    key_discarded = self.mru
                    del self.cache_data[key_discarded]
                    print('DISCARD: {}'.format(key_discarded))
                    self.cache_data[key] = item
                    self.mru = key
            else:
                self.cache_data[key] = item
                self.mru = key

    def get(self, key):
        """gets na item corresponding to key"""
        if key in self.cache_data:
            self.mru = key
            return self.cache_data[key]
