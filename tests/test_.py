

import ansible_leveldb_cache.leveldb
import shutil


def test_init():
    try:
        cache = ansible_leveldb_cache.leveldb.CacheModule()
    finally:
        cache.close()
        shutil.rmtree('/tmp/testdb/')

def test_set():
    try:
        cache = ansible_leveldb_cache.leveldb.CacheModule()
        cache.set('key', 'value')
    finally:
        cache.close()
        shutil.rmtree('/tmp/testdb/')

def test_get():
    try:
        cache = ansible_leveldb_cache.leveldb.CacheModule()
        cache.set('key', 'value')
        assert cache.get('key') == 'value'
    finally:
        cache.close()
        shutil.rmtree('/tmp/testdb/')
