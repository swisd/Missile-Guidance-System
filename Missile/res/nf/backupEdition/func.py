"""Function Backup"""
import os
import py_compile
import platform
from Missile.res import file_actions
from Missile.res import corrective_commands, ns_cwd

#compile.py
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
    else:
        with open(output, "ab") as _w:
            _w.write(current_file)

#dump.py
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

#data_injector.py
REPLACE_TXT = '*dsp//CRS_CORR.iSr,  CMD/DATA?rS CMD -LOG->'

def inject_data(data, location, position):
    """Insert Data"""
    file_actions.writefile(str(data), location)
    return position

def clear_corr():
    """Clear CORR Log"""
    file_actions.write_file_no_append(REPLACE_TXT,
                                      'C:/PyDev/Missile/log/blackbox/CRS_CORR.iSr')

def clear_dir():
    """Clear DIR Log"""
    file_actions.write_file_no_append(REPLACE_TXT,
                                      'C:/PyDev/Missile/log/blackbox/CRS_DIR.iSr')

#file_actions.py
def writefile(data: object, location: object) -> object:
    """

    :rtype: object
    :param data:
    :param location:
    """
    with open(location, "a", encoding="utf-8") as _f:
        _f.write(str(data))
        _f.close()

def write_file_no_append(ud_data: object, location: object) -> object:
    """

    :rtype: object
    :param data:
    :param location:
    """
    with open(location, "w", encoding="utf-8") as _f:
        _f.write(str(ud_data))
        _f.write('')
        _f.close()

#backup.py
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

#missile_guidance_system_main.py
def direct():
    """CWD"""
    return ns_cwd.current_relative('/system')

def stat():
    """
    Missile Setting Information
    :rtype: object
    """
    arc = 'MSL_PROG'
    curve = 'normal-UUFD'
    method = 'High Top Drop'
    path = [52, 85, 0, -65]
    print()
    print("Navigation:")
    print("  ARC: " + arc)
    print("  Curve: " + curve)
    print("  Method: " + method)
    print("  PATH: " + str(path))
    print()

def course(d_p: int, d_m: int, s_a: int) -> object:
    """
    Course-Specific Calculations
    :return:
    :rtype: int
    :param d_p:
    :param d_m:
    :param s_a:
    :return:
    """
    corrective_commands.ns_t()
    print()
    return 'Course INT:', (d_p * 2 / (d_m * d_p)) / ((d_m ** 2) / s_a)

def info():
    """
    Information about host device.
    :rtype: object
    """
    print("System Data:")
    print("  System:", platform.system())
    print("  CPU:")
    print("    CPU Cores:", os.cpu_count())
    print("    CPU Type:", "11th Gen Intel(R) Core(TM) i7-1185G7 @ 3.00 GHz")
    print("    Desc:", platform.processor())
    print("    VT:", '~_VT')
    print("    CPU Temp:", "N/A")
    print("  GPU:")
    print("    GPU Cores:", "N/A")
    print("    GPU Type:", "Intel(R) Iris(R) Xe Graphics")
    print("    VT:", '+_KT_co')
    print("    GPU Temp:", "N/A")
    print()