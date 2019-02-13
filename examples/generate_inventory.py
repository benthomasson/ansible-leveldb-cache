#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def main(args):
    for i in range(int(args[0])):
        print ("localhost{} ansible_ssh_host=127.0.0.1".format(i))

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

