"""File System Dump"""
import os
import time
from datetime import datetime

now = datetime.now()
dt_object = now.strftime("%d%m%Y%H%M%S%f%j")

directory = os.getcwd()
directory = directory.removesuffix('tools')
file_label: str = "MSL-GUID-REV2-V2.7.1-" + dt_object + '.bin'
path: str = str(directory) + '/assets/back/' + file_label
screen = False

size: int = 0


def backup(file, output):
    """
    Dump data to a file
    :param file:
    :param output:
    :return:
    """
    with open(file, "rb") as _f:
        current_file = _f.read()
    begin = "file = '" + file + "' data//"
    end = "" + " "
    
    b: bytes = bytes(begin, 'utf-8')
    e: bytes = bytes(end, 'utf-8')
    
    if not os.path.exists(output):
        with open(output, "xb") as _w:
            _w.write(b)
            _w.write(current_file)
            _w.write(e)
    else:
        with open(output, "ab") as _w:
            _w.write(b)
            _w.write(current_file)
            _w.write(e)


for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    s = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        print('[1] FILE:', f)
        size += os.path.getsize(f)
        backup(f, path)
        if screen:
            with open(f, "rb") as fil:
                print(fil.read())
    if os.path.isdir(s):
        for filename in os.listdir(s):
            f = os.path.join(s, filename)
            d = os.path.join(s, filename)
            # checking if it is a file
            if os.path.isfile(f):
                print('[2] FILE:', f)
                size += os.path.getsize(f)
                backup(f, path)
                if screen:
                    with open(f, "rb") as fil:
                        print(fil.read())
            if os.path.isdir(d):
                for filename in os.listdir(d):
                    f = os.path.join(d, filename)
                    h = os.path.join(d, filename)
                    # checking if it is a file
                    if os.path.isfile(f):
                        print('[3] FILE:', f)
                        size += os.path.getsize(f)
                        backup(f, path)
                        if screen:
                            with open(f, "rb") as fil:
                                print(fil.read())
                    if os.path.isdir(h):
                        for filename in os.listdir(h):
                            f = os.path.join(h, filename)
                            r = os.path.join(h, filename)
                            # checking if it is a file
                            if os.path.isfile(f):
                                print('[4] FILE:', f)
                                size += os.path.getsize(f)
                                backup(f, path)
                                if screen:
                                    with open(f, "rb") as fil:
                                        print(fil.read())
                            if os.path.isdir(r):
                                print('[E] DIRECTORY:', s)
                            time.sleep(0.1)
                    time.sleep(0.1)
            time.sleep(0.1)
    time.sleep(0.1)
print('Finalizing...')
time.sleep(2)
print("Backed", size, "bytes to", path)
