#! /usr/bin/env python

import sys, os

def lll('.'):
    counter_symlinks = 0
    counter_filelinks = 0
    for name in os.listdir(dirname):
        if name not in (os.curdir, os.pardir):
            full = os.path.join(dirname, name)
            if os.path.islink(full):
                counter_symlinks = counter_symlinks + 1
                if os.path.isfile(os.path.abspath(full)):
                    counter_filelinks = counter_filelinks + 1
    print(counter_symlinks)
    print(counter_filelinks)
