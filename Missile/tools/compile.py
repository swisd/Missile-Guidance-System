"""Asset Compiler"""
import os
import time
import py_compile
from datetime import datetime

directory = os.getcwd()
directory = directory.removesuffix('tools')
ITEMS = 0
l1 = 0
path: str = (directory + '/compiled/')
print("PATH:", path)
now = datetime.now()
dn_object = now.strftime("%j%z-%f")
dt_object = now.strftime("%d%m%Y%H%M%S%f%j%z")
name: str = str(ITEMS) + '-' + '63342' + '_' + str(dt_object) + '.bin'


def compress(file, output):
    """
    Compile data to a file
    :param file:
    :param output:
    :return:
    """
    py_compile.compile(file, output)


def write_to(file, output):
    """
        Write binary data to a file
        :param file:
        :param output:
        :return:
    """
    with open(file, "rb") as _f:
        current_file = _f.read()
    if (os.path.exists(output) == False):
        with open(output, "xb") as _w:
            _w.write(current_file)
            _w.close()
    else:
        with open(output, "ab") as _w:
            _w.write(current_file)
            _w.close()
    _f.close()

compress(directory + '/tools/nt', (directory + '/compiled/' + '0b0' + '/' + str(dt_object) + '/' + str(dn_object) + '/' + 'base.bin'))
write_to(directory + '/tools/nt', (directory + '/compiled/' + '0b0' + '/' + str(dt_object) + '/' + str(dn_object) + '/' + 'base.bin'))
write_to(directory + '/tools/config.ir',
         (directory + '/compiled/' + '0b0' + '/' + str(dt_object) + '/' + str(dn_object) + '/' + 'base.bin'))
for i in range(16):
    now = datetime.now()
    dt_object = now.strftime("%d%m%Y%H%M%S%f%j%z")
    dn_object = now.strftime("%j%z-%f")
    name = '63342' + '_' + str(dt_object) + '.bin'
    label = hex(l1)
    path: str = (directory + '/compiled/' + label + '/' + str(ITEMS) + '/' + str(dn_object) + '/' + name)
    full = path + "." + dt_object + ".comp.bin"
    compress(directory + '/tools/nt', (directory + '/compiled/' + '0x' + '/' + str(dt_object) +
                    '/' + str(dn_object) + '/' + str(i) + '.bin'))
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        s = os.path.join(directory, filename)
        # checking if it is a file
        if os.path.isfile(f):
            print('[1] FILE:', f)
            print(' Comp:', full)
            compress(f, full)
        
        if os.path.isdir(s):
            for filename in os.listdir(s):
                f = os.path.join(s, filename)
                d = os.path.join(s, filename)
                # checking if it is a file
                if os.path.isfile(f):
                    print('[2] FILE:', f)
                    print(' Comp:', full)
                    compress(f, full)
                
                if os.path.isdir(d):
                    for filename in os.listdir(d):
                        f = os.path.join(d, filename)
                        h = os.path.join(d, filename)
                        # checking if it is a file
                        if os.path.isfile(f):
                            print('[3] FILE:', f)
                            print(' Comp:', full)
                            compress(f, full)
                        
                        if os.path.isdir(h):
                            for filename in os.listdir(h):
                                f = os.path.join(h, filename)
                                r = os.path.join(h, filename)
                                # checking if it is a file
                                if os.path.isfile(f):
                                    print('[4] FILE:', f)
                                    print(' Comp:', full)
                                    compress(f, full)
                                
                                if os.path.isdir(r):
                                    for filename in os.listdir(r):
                                        f = os.path.join(r, filename)
                                        v = os.path.join(r, filename)
                                        # checking if it is a file
                                        if os.path.isfile(f):
                                            print('[5] FILE:', f)
                                            print(' Comp:', full)
                                            compress(f, full)
                                        
                                        if os.path.isdir(v):
                                            for filename in os.listdir(v):
                                                f = os.path.join(v, filename)
                                                l = os.path.join(v, filename)
                                                # checking if it is a file
                                                if os.path.isfile(f):
                                                    print('[6] FILE:', f)
                                                    print(' Comp:', full)
                                                    compress(f, full)
                                                
                                                if os.path.isdir(l):
                                                    for filename in os.listdir(l):
                                                        f = os.path.join(l, filename)
                                                        e = os.path.join(l, filename)
                                                        # checking if it is a file
                                                        if os.path.isfile(f):
                                                            print('[7] FILE:', f)
                                                            print(' Comp:', full)
                                                            compress(f, full)
                                                        
                                                        if os.path.isdir(e):
                                                            for filename in os.listdir(e):
                                                                f = os.path.join(e, filename)
                                                                n = os.path.join(e, filename)
                                                                # checking if it is a file
                                                                if os.path.isfile(f):
                                                                    print('[8] FILE:', f)
                                                                    print(' Comp:', full)
                                                                    compress(f, full)
                                                                
                                                                if os.path.isdir(n):
                                                                    print('[E] DIRECTORY:', s)
                                                                ITEMS += 1
                                                                # time.sleep(0.01)
                                                        ITEMS += 1
                                                        # time.sleep(0.001)
                                                ITEMS += 1
                                                # time.sleep(0.001)
                                        ITEMS += 1
                                        # time.sleep(0.001)
                                ITEMS += 1
                                # time.sleep(0.001)
                        ITEMS += 1
                        # time.sleep(0.001)
                ITEMS += 1
                # time.sleep(0.001)
        ITEMS += 1
        # time.sleep(0.001)
    l1 += 1
time.sleep(0.001)
l1 = 0
ITEMS = 0
for i in range(16):
    now = datetime.now()
    dt_object = now.strftime("%d%m%Y%H%M%S%f%j%z")
    dn_object = now.strftime("%j%z-%f")
    name = '63342' + '_' + str(dt_object) + '.bin'
    label = hex(l1)
    path: str = (directory + '/compiled/' + label + '/' + str(ITEMS) + '/' + str(dn_object) + '/' + name)
    full = path + "." + dt_object + ".comp.bin"
    compress(directory + '/tools/nt', (directory + '/compiled/' + '1x' + '/' + str(dt_object) +
                    '/' + str(dn_object) + '/' + str(i) + '.bin'))
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        s = os.path.join(directory, filename)
        # checking if it is a file
        if os.path.isfile(f):
            print('[1] FILE:', f)
            compress(directory + '/tools/nt', full)
            write_to(f, full)
        
        if os.path.isdir(s):
            for filename in os.listdir(s):
                f = os.path.join(s, filename)
                d = os.path.join(s, filename)
                # checking if it is a file
                if os.path.isfile(f):
                    print('[2] FILE:', f)
                    print('   To:', full)
                    compress(directory + '/tools/nt', full)
                    write_to(f, full)
                
                if os.path.isdir(d):
                    for filename in os.listdir(d):
                        f = os.path.join(d, filename)
                        h = os.path.join(d, filename)
                        # checking if it is a file
                        if os.path.isfile(f):
                            print('[3] FILE:', f)
                            print('   To:', full)
                            compress(directory + '/tools/nt', full)
                            write_to(f, full)
                        
                        if os.path.isdir(h):
                            for filename in os.listdir(h):
                                f = os.path.join(h, filename)
                                r = os.path.join(h, filename)
                                # checking if it is a file
                                if os.path.isfile(f):
                                    print('[4] FILE:', f)
                                    print('   To:', full)
                                    compress(directory + '/tools/nt', full)
                                    write_to(f, full)
                                
                                if os.path.isdir(r):
                                    for filename in os.listdir(r):
                                        f = os.path.join(r, filename)
                                        v = os.path.join(r, filename)
                                        # checking if it is a file
                                        if os.path.isfile(f):
                                            print('[5] FILE:', f)
                                            print('   To:', full)
                                            compress(directory + '/tools/nt', full)
                                            write_to(f, full)
                                        
                                        if os.path.isdir(v):
                                            for filename in os.listdir(v):
                                                f = os.path.join(v, filename)
                                                l = os.path.join(v, filename)
                                                # checking if it is a file
                                                if os.path.isfile(f):
                                                    print('[6] FILE:', f)
                                                    print('   To:', full)
                                                    compress(directory + '/tools/nt', full)
                                                    write_to(f, full)
                                                
                                                if os.path.isdir(l):
                                                    for filename in os.listdir(l):
                                                        f = os.path.join(l, filename)
                                                        e = os.path.join(l, filename)
                                                        # checking if it is a file
                                                        if os.path.isfile(f):
                                                            print('[7] FILE:', f)
                                                            print('   To:', full)
                                                            compress(directory + '/tools/nt', full)
                                                            write_to(f, full)
                                                        
                                                        if os.path.isdir(e):
                                                            for filename in os.listdir(e):
                                                                f = os.path.join(e, filename)
                                                                n = os.path.join(e, filename)
                                                                # checking if it is a file
                                                                if os.path.isfile(f):
                                                                    print('[8] FILE:', f)
                                                                    print('   To:', full)
                                                                    compress(directory + '/tools/nt', full)
                                                                    write_to(f, full)
                                                                
                                                                if os.path.isdir(n):
                                                                    print('[E] DIRECTORY:', s)
                                                                ITEMS += 1
                                                                # time.sleep(0.01)
                                                        ITEMS += 1
                                                        # time.sleep(0.001)
                                                ITEMS += 1
                                                # time.sleep(0.001)
                                        ITEMS += 1
                                        # time.sleep(0.001)
                                ITEMS += 1
                                # time.sleep(0.001)
                        ITEMS += 1
                        # time.sleep(0.001)
                ITEMS += 1
                # time.sleep(0.001)
        ITEMS += 1
        # time.sleep(0.001)
    l1 += 1
time.sleep(0.001)

print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print('Compile complete.')
