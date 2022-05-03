#!/usr/bin/env python3
"""LRU Caching"""
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """LRU Caching system"""
    def __init__(self):
        """initialises the calss instance"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """adds item value corresponding to key
        the method move_to_end moves key to end to access lru
        """
        if key and item:
            self.cache_data[key] = item
            self.cache_data.move_to_end(key)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            key_discarded = self.cache_data.popitem(last=False)
            print('DISCARD: {}'.format(discarded[0]))

    def get(self, key):
        """gets an item corresponding to key"""
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
