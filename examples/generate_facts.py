#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import json

def main(args):
    data = {}
    for i in range(int(args[0])):
        data["data{}".format(i)] = "1234567890" * 1000
    print (json.dumps(data))

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))


