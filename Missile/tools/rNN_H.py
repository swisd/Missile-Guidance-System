"""rNN-H File Comp"""
import py_compile

import os
import time
from datetime import datetime

import Missile



iterate = 0
now = datetime.now()
dt_object = now.strftime("%d%m%Y%H%M%S%f%j")

directory = os.getcwd()
directory = directory.removesuffix('tools')
modelsDIR = directory + '/assets/models/missiles/'
launchersDIR = directory + '/assets/models/launchers/'
targetsDIR = directory + '/assets/models/targets/'
file_label = ''
path: str = str(directory) + '/rNN/' + Missile.__version__ + '/' + file_label + '.pth'
bins: str = str(directory) + '/rNN/' + Missile.__version__ + '/' + file_label + '.bin'
comp: str = str(directory) + '/rNN/' + Missile.__version__ + '/' + file_label + '.dnsc'
flex: str = str(directory) + '/rNN/' + Missile.__version__ + '/' + file_label + '.flex'
if not os.path.exists(Missile.__version__) == True:
    os.makedirs(directory + '/rNN/' + Missile.__version__)
    if not os.path.exists('/missiles/'):
        os.makedirs(directory + '/rNN/' + Missile.__version__ + '/missiles/')
    else:
        pass
    if not os.path.exists('/launchers/'):
        os.makedirs(directory + '/rNN/' + Missile.__version__ + '/launchers/')
    else:
        pass
    if not os.path.exists('/targets/'):
        os.makedirs(directory + '/rNN/' + Missile.__version__ + '/targets/')
    else:
        pass
    if not os.path.exists('/indexes/'):
        os.makedirs(directory + '/rNN/' + Missile.__version__ + '/indexes/')
    else:
        pass
else:
    pass
screen = False

size: int = 0


def compress(file, output):
    """
    Compile data to a file
    :param file:
    :param output:
    :return:
    """
    py_compile.compile(file, output)


def out(file: object, output: object, mode: object) -> object:
    """
    Dump data to a file BS+1
    :type mode: object
    :param file:
    :param output:
    :return:
    """
    # todo: encryption updates for proper encryption to .pth files
    if 'dnsc-pth' == mode:
        with open(file, "rb") as _f:
           current_file = _f.read()

        vn = str(current_file, encoding='utf-16-le', errors='ignore') # Ignore errors on exception

        if not os.path.exists(output):
            with open(output, "xb") as _x:
                _x.write(bytes(vn, encoding='utf-16-be', errors='ignore')) # Ignore errors on exception
                _x.close()
        else:
            with open(output, "wb") as _w:
                _w.write(bytes(vn, encoding='utf-16-be', errors='ignore')) # Ignore errors on exception
                _w.close()
        _f.close()
    elif mode == 'bin-flex':
        with open(file, "rb") as _f:
           current_file = _f.read()

        vn = str(current_file, encoding='utf-16-be', errors='ignore') # Ignore errors on exception

        if not os.path.exists(output):
            with open(output, "xb") as _x:
                _x.write(bytes(vn, encoding='utf-16-le', errors='ignore')) # Ignore errors on exception
                _x.close()
        else:
            with open(output, "wb") as _w:
                _w.write(bytes(vn, encoding='utf-16-le', errors='ignore')) # Ignore errors on exception
                _w.close()
        _f.close()

for filename in os.listdir(modelsDIR):
    iterate += 1
    f = os.path.join(modelsDIR, filename)
    # checking if it is a file
    if os.path.isfile(f):
        file_label = filename
        path: str = str(directory) + '/rNN/' + str(Missile.__version__) + '/missiles/' + file_label + '.pth'
        bins: str = str(directory) + '/rNN/' + str(Missile.__version__) + '/missiles/' + file_label + '.bin'
        comp: str = str(directory) + '/rNN/' + str(Missile.__version__) + '/missiles/' + file_label + '.dnsc'
        flex: str = str(directory) + '/rNN/' + str(Missile.__version__) + '/missiles/' + file_label + '.flex'
        nlist: str = str(directory) + '/rNN/' + str(Missile.__version__) + '/indexes/index' + str(iterate) + '.i'

        with open('disklist.e.idl', "w+") as ns:
            ns.write(path + "\n")
            ns.write(bins + "\n")
            ns.write(comp + "\n")
            ns.write(flex + "\n")
            ns.write(nlist + "\n")
            ns.write('__os:__nt__')

        print('[1] FILE:', f)
        size += os.path.getsize(f)
        out('disklist.e.idl', nlist, mode='bin-flex')

    time.sleep(0.05)
print('Compressing...')
time.sleep(2)
for filename in os.listdir(modelsDIR):
    f = os.path.join(modelsDIR, filename)
    # checking if it is a file
    if os.path.isfile(f):
        file_label = filename
        path: str = str(directory) + '/rNN/' + str(Missile.__version__) + '/missiles/' + file_label + '.pth'
        bins: str = str(directory) + '/rNN/' + str(Missile.__version__) + '/missiles/' + file_label + '.bin'
        comp: str = str(directory) + '/rNN/' + str(Missile.__version__) + '/missiles/' + file_label + '.dnsc'
        flex: str = str(directory) + '/rNN/' + str(Missile.__version__) + '/missiles/' + file_label + '.flex'

        print('[1] FILE:', f)
        size += os.path.getsize(f)
        out(f, path, mode='dnsc-pth')
        out(f, bins, mode='bin-flex')
        out(f, comp, mode='dnsc-pth')
        out(f, flex, mode='bin-flex')
    time.sleep(0.05)
print('Finalizing...')
time.sleep(2)

for filename in os.listdir(targetsDIR):
    iterate += 1
    f = os.path.join(targetsDIR, filename)
    # checking if it is a file
    if os.path.isfile(f):
        file_label = filename
        path: str = str(directory) + '/rNN/' + str(Missile.__version__) + '/targets/' + file_label + '.pth'
        bins: str = str(directory) + '/rNN/' + str(Missile.__version__) + '/targets/' + file_label + '.bin'
        comp: str = str(directory) + '/rNN/' + str(Missile.__version__) + '/targets/' + file_label + '.dnsc'
        flex: str = str(directory) + '/rNN/' + str(Missile.__version__) + '/targets/' + file_label + '.flex'
        nlist: str = str(directory) + '/rNN/' + str(Missile.__version__) + '/indexes/index' + str(iterate) + '.i'

        with open('disklist.e.idl', "w+") as ns:
            ns.write(path + "\n")
            ns.write(bins + "\n")
            ns.write(comp + "\n")
            ns.write(flex + "\n")
            ns.write(nlist + "\n")
            ns.write('__os:__nt__')

        print('[1] FILE:', f)
        size += os.path.getsize(f)
        out('disklist.e.idl', nlist, mode='bin-flex')

    time.sleep(0.05)
print('Compressing...')
time.sleep(2)
for filename in os.listdir(targetsDIR):
    f = os.path.join(targetsDIR, filename)
    # checking if it is a file
    if os.path.isfile(f):
        file_label = filename
        path: str = str(directory) + '/rNN/' + str(Missile.__version__) + '/targets/' + file_label + '.pth'
        bins: str = str(directory) + '/rNN/' + str(Missile.__version__) + '/targets/' + file_label + '.bin'
        comp: str = str(directory) + '/rNN/' + str(Missile.__version__) + '/targets/' + file_label + '.dnsc'
        flex: str = str(directory) + '/rNN/' + str(Missile.__version__) + '/targets/' + file_label + '.flex'

        print('[1] FILE:', f)
        size += os.path.getsize(f)
        out(f, path, mode='dnsc-pth')
        out(f, bins, mode='bin-flex')
        out(f, comp, mode='dnsc-pth')
        out(f, flex, mode='bin-flex')
    time.sleep(0.05)
print('Finalizing...')
time.sleep(2)

for filename in os.listdir(launchersDIR):
    iterate += 1
    f = os.path.join(launchersDIR, filename)
    # checking if it is a file
    if os.path.isfile(f):
        file_label = filename
        path: str = str(directory) + '/rNN/' + str(Missile.__version__) + '/launchers/' + file_label + '.pth'
        bins: str = str(directory) + '/rNN/' + str(Missile.__version__) + '/launchers/' + file_label + '.bin'
        comp: str = str(directory) + '/rNN/' + str(Missile.__version__) + '/launchers/' + file_label + '.dnsc'
        flex: str = str(directory) + '/rNN/' + str(Missile.__version__) + '/launchers/' + file_label + '.flex'
        nlist: str = str(directory) + '/rNN/' + str(Missile.__version__) + '/indexes/index' + str(iterate) + '.i'

        with open('disklist.e.idl', "w+") as ns:
            ns.write(path + "\n")
            ns.write(bins + "\n")
            ns.write(comp + "\n")
            ns.write(flex + "\n")
            ns.write(nlist + "\n")
            ns.write('__os:__nt__')

        print('[1] FILE:', f)
        size += os.path.getsize(f)
        out('disklist.e.idl', nlist, mode='bin-flex')

    time.sleep(0.05)
print('Compressing...')
time.sleep(2)
for filename in os.listdir(launchersDIR):
    f = os.path.join(launchersDIR, filename)
    # checking if it is a file
    if os.path.isfile(f):
        file_label = filename
        path: str = str(directory) + '/rNN/' + str(Missile.__version__) + '/launchers/' + file_label + '.pth'
        bins: str = str(directory) + '/rNN/' + str(Missile.__version__) + '/launchers/' + file_label + '.bin'
        comp: str = str(directory) + '/rNN/' + str(Missile.__version__) + '/launchers/' + file_label + '.dnsc'
        flex: str = str(directory) + '/rNN/' + str(Missile.__version__) + '/launchers/' + file_label + '.flex'

        print('[1] FILE:', f)
        size += os.path.getsize(f)
        out(f, path, mode='dnsc-pth')
        out(f, bins, mode='bin-flex')
        out(f, comp, mode='dnsc-pth')
        out(f, flex, mode='bin-flex')
    time.sleep(0.05)
print('Finalizing...')
time.sleep(2)
