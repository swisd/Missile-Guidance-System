"""NS Repair Tool"""
import os

import time
corrupted = bool(input(""))
#corrupted: bool = False
files = ("Missile\log/blackbox\controller/ns-controller.cs", "Missile\log/blackbox\controller/ns-nt-controller.uskx")
progress = ''
cfile = ''
directory = os.getcwd()
directory = directory.removesuffix('tools')
print(directory)
count = 0

print("Scanning")
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    s = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        print('[1] FILE:', f)
        count += 1
    if os.path.isdir(s):
        for filename in os.listdir(s):
            f = os.path.join(s, filename)
            d = os.path.join(s, filename)
            # checking if it is a file
            if os.path.isfile(f):
                print('[2] FILE:', f)
                count += 1
            if os.path.isdir(d):
                for filename in os.listdir(d):
                    f = os.path.join(d, filename)
                    h = os.path.join(d, filename)
                    # checking if it is a file
                    if os.path.isfile(f):
                        print('[3] FILE:', f)
                        count += 1
                    if os.path.isdir(h):
                        for filename in os.listdir(h):
                            f = os.path.join(h, filename)
                            r = os.path.join(h, filename)
                            # checking if it is a file
                            if os.path.isfile(f):
                                print('[4] FILE:', f)
                                count += 1
                            if os.path.isdir(r):
                                print('[E] DIRECTORY:', s)
                            time.sleep(0.1)
                    time.sleep(0.1)
            time.sleep(0.1)
    time.sleep(0.1)
progress = ''
for i in range(3):
    progress += '-'
    print(f'\r{cfile + progress}', end='')
    time.sleep(0.25)
print()


if corrupted == True:
    print("Corrupted files detected.")
    for file in files:
        print(file)
    print("Repair? Y/N")
    REPAIR = str(input(">"))
    if REPAIR == 'Y':
        progress = ''
        print("Fixing Errors")
        for i in range(count):
            progress =  '-' * ((round(((i + 1)/count)*10)))
            cfile = files[0]
            print(f'\r{progress}', end='')
            time.sleep(0.25)
        print()
        print("Reindexing")
        for filename in os.listdir(directory):
            f = os.path.join(directory, filename)
            s = os.path.join(directory, filename)
            # checking if it is a file
            if os.path.isfile(f):
                print('[1] FILE:', f)
            if os.path.isdir(s):
                for filename in os.listdir(s):
                    f = os.path.join(s, filename)
                    d = os.path.join(s, filename)
                    # checking if it is a file
                    if os.path.isfile(f):
                        print('[2] FILE:', f)
                    if os.path.isdir(d):
                        for filename in os.listdir(d):
                            f = os.path.join(d, filename)
                            h = os.path.join(d, filename)
                            # checking if it is a file
                            if os.path.isfile(f):
                                print('[3] FILE:', f)
                            if os.path.isdir(h):
                                for filename in os.listdir(h):
                                    f = os.path.join(h, filename)
                                    r = os.path.join(h, filename)
                                    # checking if it is a file
                                    if os.path.isfile(f):
                                        print('[4] FILE:', f)
                                    if os.path.isdir(r):
                                        print('[E] DIRECTORY:', s)
                                    time.sleep(0.1)
                            time.sleep(0.1)
                    time.sleep(0.1)
            time.sleep(0.1)
        progress = ''
        for i in range(3):
            progress += '-'
            print(f'\r{progress}', end='')
            time.sleep(0.25)
    else:
        print("Corrupted files may render the system unstable.")
else:
    print("No corrupted files detected.")