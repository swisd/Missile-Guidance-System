"""File System Dump"""
import os
import time
from datetime import datetime

now = datetime.now()
dt_object = now.strftime("%d%m%Y_%H%M%S")

directory = os.getcwd()
directory = directory.removesuffix('tools')
file_label: str = "nf_dump-" + str(dt_object) +  "(V2.7.0)" + '.bin'
path: str = str(os.getcwd()) + '/dumps/' + file_label


size: int = 0
def dump(file, output):
    """
    Dump data to a file
    :param file:
    :param output:
    :return:
    """
    with open(file, "rb") as _f:
        current_file = _f.read()
    if not os.path.exists(output) == True:
        with open(output, "xb") as _w:
            _w.write(current_file)
    else:
        with open(output, "ab") as _w:
            _w.write(current_file)




for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    s = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        print('[1] FILE:', f)
        size += os.path.getsize(f)
        dump(f, path)
    if os.path.isdir(s):
        for filename in os.listdir(s):
            f = os.path.join(s, filename)
            d = os.path.join(s, filename)
            # checking if it is a file
            if os.path.isfile(f):
                print('[2] FILE:', f)
                size += os.path.getsize(f)
                dump(f, path)
            if os.path.isdir(d):
                for filename in os.listdir(d):
                    f = os.path.join(d, filename)
                    h = os.path.join(d, filename)
                    # checking if it is a file
                    if os.path.isfile(f):
                        print('[3] FILE:', f)
                        size += os.path.getsize(f)
                        dump(f, path)
                    if os.path.isdir(h):
                        for filename in os.listdir(h):
                            f = os.path.join(h, filename)
                            r = os.path.join(h, filename)
                            # checking if it is a file
                            if os.path.isfile(f):
                                print('[4] FILE:', f)
                                size += os.path.getsize(f)
                                dump(f, path)
                            if os.path.isdir(r):
                                print('[E] DIRECTORY:', s)
                            time.sleep(0.1)
                    time.sleep(0.1)
            time.sleep(0.1)
    time.sleep(0.1)
print('Finalizing...')
time.sleep(2)
print("Dumped", size, "bytes to", path)
    
