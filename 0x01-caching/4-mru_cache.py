#!/usr/bin/env python3
"""MRU caching"""
from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """MRU Caching System"""
    def __init__(self):
        """initialises the class instance"""
        super().__init__()
        self.cache_data = OrderedDict()
        self.mru = ""

    def put(self, key, item):
        """assigns item value corresponding to key"""
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if key in self.cache_data:
                    self.cache_data.update({key: item})
                    self.mru = key
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
        """gets an item corresponding to key"""
        if key in self.cache_data:
            self.mru = key
            return self.cache_data[key]
