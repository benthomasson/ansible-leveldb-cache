from __future__ import print_function
from ansible.plugins.cache import BaseCacheModule
import json
import os

DOCUMENTATION = '''
    cache: leveldb
'''


class CacheModule(BaseCacheModule):

    def __init__(self, *args, **kwargs):
        print('args {}'.format(args))
        print('kwargs {}'.format(kwargs))
        self._cache = '/tmp/test_multiple'
        if not os.path.exists(self._cache):
            os.makedirs(self._cache)

    def get(self, key):
        print('get {}'.format(key))
        with open(os.path.join(self._cache, key)) as f:
            return json.loads(f.read())

    def set(self, key, value):
        print('set {}'.format(key))
        with open(os.path.join(self._cache, key), 'w') as f:
            f.write(json.dumps(value))

    def keys(self):
        print('keys')
        return os.listdir(self._cache)

    def contains(self, key):
        print('contains {}'.format(key.encode()))
        return os.path.exists(os.path.join(self._cache, key))

    def delete(self, key):
        print('delete {}'.format(key.encode()))
        return os.unlink(os.path.join(self._cache, key))

    def flush(self):
        print('flush')
        for key in self.keys():
            self.delete(key)

    def copy(self):
        print('copy')
        raise Exception('copy called')

    def __getstate__(self):
        print('getstate')
        raise Exception('getstate called')

    def __setstate__(self, data):
        print('setstate')
        raise Exception('setstate called')
