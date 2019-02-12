#!/usr/bin/env python
# -*- coding: utf-8 -*-

import plyvel
import sys
import ansible_leveldb_cache.leveldb

def main(args):

    cache = ansible_leveldb_cache.leveldb.CacheModule()
    for key in cache.keys():
        print ("key {} value {}".format(key, cache.get(key)))
    print ('num keys {}'.format(len(cache.keys())))

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))




