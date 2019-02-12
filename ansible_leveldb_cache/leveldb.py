from __future__ import print_function
import plyvel
from ansible.plugins.cache import BaseCacheModule
import json

DOCUMENTATION = '''
    cache: leveldb
'''


class CacheModule(BaseCacheModule):

    def __init__(self, *args, **kwargs):
        print ('args {}'.format(args))
        print ('kwargs {}'.format(kwargs))
        self._cache = plyvel.DB('/tmp/testdb/', create_if_missing=True)

    def get(self, key):
        print ('get {}'.format(key))
        return json.loads(self._cache.get(key.encode()).decode())

    def set(self, key, value):
        print ('set {}'.format(key))
        return self._cache.put(key.encode(), json.dumps(value).encode())

    def keys(self):
        print ('keys')
        return [key.decode() for key in list(self._cache.iterator(include_value=False))]

    def contains(self, key):
        print ('contains {}'.format(key.encode()))
        return self._cache.get(key.encode()) is not None

    def delete(self, key):
        print ('delete {}'.format(key.encode()))
        return self._cache.delete(key)

    def flush(self):
        print ('flush')
        for key in self.keys():
            self.delete(key)

    def close(self):
        print ('close')
        self._cache.close()

    def copy(self):
        print ('copy')
        raise Exception('copy called')

    def __getstate__(self):
        print ('getstate')
        raise Exception('getstate called')

    def __setstate__(self, data):
        print ('setstate')
        raise Exception('setstate called')
