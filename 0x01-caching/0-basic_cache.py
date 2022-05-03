#!/usr/bin/ev python3
"""basic dictionary"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """dictionary caching"""
    def put(self, key, item):
        """adds item in cache"""
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """Get an item using key"""
        return self.cache_data.get(key)
