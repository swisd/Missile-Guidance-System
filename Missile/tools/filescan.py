"""File System Reader"""
import os
import time
directory = os.getcwd()
directory = directory.removesuffix('tools')
print()

print("Current Working Directory ", str(directory))
print("Current File Directory ", str(directory) + "/")

# assign directory

DIRECT = 0
ITEMS = 0
PYFILE = 0
BINS = 0
PYCFILE = 0
OTHERFILE = 0
TOTALSIZE = 0
AVAILABLE = 0
UNAVAILABLE = 0
MSMDFILE = 0
ISRDATA = 0
UNREACHABLE = 0

# iterate over files in
# that directory
# return filepath in
# every directory

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    s = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        print('[1] FILE:', f)
        TOTALSIZE += os.path.getsize(f)
        if os.path.exists(f):
            AVAILABLE += 1
        else:
            UNAVAILABLE += 1
        if '.py' in f:
            PYFILE += 1
        if '.bin' in f:
            BINS += 1
        if '.pyc' in f:
            PYCFILE += 1
        if '.iSr' in f:
            ISRDATA += 1
        if '.msl' in f:
            MSMDFILE += 1
        else:
            OTHERFILE += 1
    if os.path.isdir(s):
        DIRECT += 1
        for filename in os.listdir(s):
            f = os.path.join(s, filename)
            d = os.path.join(s, filename)
            # checking if it is a file
            if os.path.isfile(f):
                print('[2] FILE:', f)
                TOTALSIZE += os.path.getsize(f)
                if os.path.exists(f):
                    AVAILABLE += 1
                else:
                    UNAVAILABLE += 1
                if '.py' in f:
                    PYFILE += 1
                if '.bin' in f:
                    BINS += 1
                if '.pyc' in f:
                    PYCFILE += 1
                if '.iSr' in f:
                    ISRDATA += 1
                if '.msl' in f:
                    MSMDFILE += 1
                else:
                    OTHERFILE += 1
            if os.path.isdir(d):
                DIRECT += 1
                for filename in os.listdir(d):
                    f = os.path.join(d, filename)
                    h = os.path.join(d, filename)
                    # checking if it is a file
                    if os.path.isfile(f):
                        print('[3] FILE:', f)
                        TOTALSIZE += os.path.getsize(f)
                        if os.path.exists(f):
                            AVAILABLE += 1
                        else:
                            UNAVAILABLE += 1
                        if '.py' in f:
                            PYFILE += 1
                        if '.bin' in f:
                            BINS += 1
                        if '.pyc' in f:
                            PYCFILE += 1
                        if '.iSr' in f:
                            ISRDATA += 1
                        if '.msl' in f:
                            MSMDFILE += 1
                        else:
                            OTHERFILE += 1
                    if os.path.isdir(h):
                        DIRECT += 1
                        for filename in os.listdir(h):
                            f = os.path.join(h, filename)
                            r = os.path.join(h, filename)
                            # checking if it is a file
                            if os.path.isfile(f):
                                print('[4] FILE:', f)
                                TOTALSIZE += os.path.getsize(f)
                                if os.path.exists(f):
                                    AVAILABLE += 1
                                else:
                                    UNAVAILABLE += 1
                                if '.py' in f:
                                    PYFILE += 1
                                if '.bin' in f:
                                    BINS += 1
                                if '.pyc' in f:
                                    PYCFILE += 1
                                if '.iSr' in f:
                                    ISRDATA += 1
                                if '.msl' in f:
                                    MSMDFILE += 1
                                else:
                                    OTHERFILE += 1
                            if os.path.isdir(r):
                                DIRECT += 1
                                for filename in os.listdir(r):
                                    f = os.path.join(r, filename)
                                    v = os.path.join(r, filename)
                                    # checking if it is a file
                                    if os.path.isfile(f):
                                        print('[5] FILE:', f)
                                        TOTALSIZE += os.path.getsize(f)
                                        if os.path.exists(f):
                                            AVAILABLE += 1
                                        else:
                                            UNAVAILABLE += 1
                                        if '.py' in f:
                                            PYFILE += 1
                                        if '.bin' in f:
                                            BINS += 1
                                        if '.pyc' in f:
                                            PYCFILE += 1
                                        if '.iSr' in f:
                                            ISRDATA += 1
                                        if '.msl' in f:
                                            MSMDFILE += 1
                                        else:
                                            OTHERFILE += 1
                                    if os.path.isdir(v):
                                        DIRECT += 1
                                        for filename in os.listdir(v):
                                            f = os.path.join(v, filename)
                                            l = os.path.join(v, filename)
                                            # checking if it is a file
                                            if os.path.isfile(f):
                                                print('[6] FILE:', f)
                                                TOTALSIZE += os.path.getsize(f)
                                                if os.path.exists(f):
                                                    AVAILABLE += 1
                                                else:
                                                    UNAVAILABLE += 1
                                                if '.py' in f:
                                                    PYFILE += 1
                                                if '.bin' in f:
                                                    BINS += 1
                                                if '.pyc' in f:
                                                    PYCFILE += 1
                                                if '.iSr' in f:
                                                    ISRDATA += 1
                                                if '.msl' in f:
                                                    MSMDFILE += 1
                                                else:
                                                    OTHERFILE += 1
                                            if os.path.isdir(l):
                                                DIRECT += 1
                                                for filename in os.listdir(l):
                                                    f = os.path.join(l, filename)
                                                    e = os.path.join(l, filename)
                                                    # checking if it is a file
                                                    if os.path.isfile(f):
                                                        print('[7] FILE:', f)
                                                        TOTALSIZE += os.path.getsize(f)
                                                        if os.path.exists(f):
                                                            AVAILABLE += 1
                                                        else:
                                                            UNAVAILABLE += 1
                                                        if '.py' in f:
                                                            PYFILE += 1
                                                        if '.bin' in f:
                                                            BINS += 1
                                                        if '.pyc' in f:
                                                            PYCFILE += 1
                                                        if '.iSr' in f:
                                                            ISRDATA += 1
                                                        if '.msl' in f:
                                                            MSMDFILE += 1
                                                        else:
                                                            OTHERFILE += 1
                                                    if os.path.isdir(e):
                                                        DIRECT += 1
                                                        for filename in os.listdir(e):
                                                            f = os.path.join(e, filename)
                                                            n = os.path.join(e, filename)
                                                            # checking if it is a file
                                                            if os.path.isfile(f):
                                                                print('[8] FILE:', f)
                                                                TOTALSIZE += os.path.getsize(f)
                                                                if os.path.exists(f):
                                                                    AVAILABLE += 1
                                                                else:
                                                                    UNAVAILABLE += 1
                                                                if '.py' in f:
                                                                    PYFILE += 1
                                                                if '.bin' in f:
                                                                    BINS += 1
                                                                if '.pyc' in f:
                                                                    PYCFILE += 1
                                                                if '.iSr' in f:
                                                                    ISRDATA += 1
                                                                if '.msl' in f:
                                                                    MSMDFILE += 1
                                                                else:
                                                                    OTHERFILE += 1
                                                            if os.path.isdir(n):
                                                                print('[E] DIRECTORY:', s)
                                                                UNREACHABLE += 1
                                                                DIRECT += 1
                                                            ITEMS += 1
                                                            #time.sleep(0.01)
                                                    ITEMS += 1
                                                    #time.sleep(0.001)
                                            ITEMS += 1
                                            #time.sleep(0.001)
                                    ITEMS += 1
                                    #time.sleep(0.001)
                            ITEMS += 1
                            #time.sleep(0.001)
                    ITEMS += 1
                    #time.sleep(0.001)
            ITEMS += 1
            #time.sleep(0.001)
    ITEMS += 1
    #time.sleep(0.001)
print()
print("--------------------------------------------")
print("              Results Summary               ")
print("--------------------------------------------")
print("#Items:", ITEMS)
print("--------------------------------------------")
print("PY Files:", PYFILE)
print("Binaries:", BINS)
print("PYCompiled Files:", PYCFILE)
print("Missile Model Files:", MSMDFILE)
print("iSr Blackbox Files:", ISRDATA)
print("Other Filetypes:", OTHERFILE)
print("Directories:", DIRECT)
print("--------------------------------------------")
print("Size on Disk:", TOTALSIZE, 'bytes  (B,o)')
print("--------------------------------------------")
print("Available:", AVAILABLE)
print("Unavailable:", UNAVAILABLE)
print("Unreachable (Past Level): >=", UNREACHABLE)
print("--------------------------------------------")
