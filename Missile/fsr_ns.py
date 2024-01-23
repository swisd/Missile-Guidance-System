"""File System Reader"""
import os
import time

print()

print("Current Working Directory ", str(os.getcwd()))
print("Current File Directory ", str(os.getcwd()) + "/")

# assign directory
directory = os.getcwd()

# iterate over files in
# that directory
items = 0
pyfile = 0
bins = 0
pycfile = 0
otherfile = 0
totalsize = 0
available = 0
unavailable = 0
msmdfile = 0
isrdata = 0

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    s = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        print('FILE:', f)
        totalsize += os.path.getsize(f)
        if os.path.exists(f):
            available += 1
        else:
            unavailable += 1
        if '.py' in f:
            pyfile += 1
        if '.bin' in f:
            bins += 1
        if '.pyc' in f:
            pycfile += 1
        if '.iSr' in f:
            isrdata += 1
        if '.msl' in f:
            msmdfile += 1
        else:
            otherfile += 1
    if os.path.isdir(s):
        for filename in os.listdir(s):
            f = os.path.join(s, filename)
            d = os.path.join(s, filename)
            # checking if it is a file
            if os.path.isfile(f):
                print('FILE:', f)
                totalsize += os.path.getsize(f)
                if os.path.exists(f):
                    available += 1
                else:
                    unavailable += 1
                if '.py' in f:
                    pyfile += 1
                if '.bin' in f:
                    bins += 1
                if '.pyc' in f:
                    pycfile += 1
                if '.iSr' in f:
                    isrdata += 1
                if '.msl' in f:
                    msmdfile += 1
                else:
                    otherfile += 1
            if os.path.isdir(d):
                for filename in os.listdir(d):
                    f = os.path.join(d, filename)
                    h = os.path.join(d, filename)
                    # checking if it is a file
                    if os.path.isfile(f):
                        print('FILE:', f)
                        totalsize += os.path.getsize(f)
                        if os.path.exists(f):
                            available += 1
                        else:
                            unavailable += 1
                        if '.py' in f:
                            pyfile += 1
                        if '.bin' in f:
                            bins += 1
                        if '.pyc' in f:
                            pycfile += 1
                        if '.iSr' in f:
                            isrdata += 1
                        if '.msl' in f:
                            msmdfile += 1
                        else:
                            otherfile += 1
                    if os.path.isdir(h):
                        for filename in os.listdir(h):
                            f = os.path.join(h, filename)
                            r = os.path.join(h, filename)
                            # checking if it is a file
                            if os.path.isfile(f):
                                print('FILE:', f)
                                totalsize += os.path.getsize(f)
                                if os.path.exists(f):
                                    available += 1
                                else:
                                    unavailable += 1
                                if '.py' in f:
                                    pyfile += 1
                                if '.bin' in f:
                                    bins += 1
                                if '.pyc' in f:
                                    pycfile += 1
                                if '.iSr' in f:
                                    isrdata += 1
                                if '.msl' in f:
                                    msmdfile += 1
                                else:
                                    otherfile += 1
                            if os.path.isdir(r):
                                print('DIRECTORY:', s)
                            time.sleep(0.05)
                            items += 1
                    time.sleep(0.05)
                    items += 1
            time.sleep(0.05)
            items += 1
    time.sleep(0.05)
    items += 1
print()
print("--------------------------------------------")
print("              Results Summary               ")
print("--------------------------------------------")
print("#Items:", items)
print("--------------------------------------------")
print("PY Files:", pyfile)
print("Binaries:", bins)
print("PYCompiled Files:", pycfile)
print("Missile Model Files:", msmdfile)
print("iSr Blackbox Files:", isrdata)
print("Other Filetypes:", otherfile)
print("--------------------------------------------")
print("Size on Disk:", totalsize, 'bytes')
print("--------------------------------------------")
print("Available:", available)
print("Unavailable:", unavailable)
print("--------------------------------------------")
