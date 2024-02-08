"""Missile Guidance System UI"""
import os
import platform
import time
from Missile.res import file_actions, define, corrective_commands, ns_cwd
import Missile
import tkinter as tk
from tkinter import *
from tkinter import messagebox

virt_alt: int = 1
valueError: str = "Error. Impossible values."
CONSTANTS = define.CONSTANTS
missile_list = ['DTR-45D', 'AGMX 354-H', 'ICBCM-ATCS 152A/C']
directory = os.getcwd()
directory = directory.removesuffix('system')
"""
For use in future developments.
pitch = 0
roll = 0
yaw = 0
"""

alt: int = 0
"""
spd = 0"""
THR = 0
"""
ws = [0, 0]
atp = 14.7  # ASL
eng_ves_a = 0
eng_vec_b = 0
"""
VERSION = Missile.__version__
REVISION = Missile.__revision__
NAME = Missile.__name__
AUTHOR = Missile.__author__


def direct(a_d: str):
    """CWD
    :type a_d: object
    """
    return ns_cwd.current_relative(a_d)


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


def error():
    """
    Value Error
    """
    print(valueError)


# DPS, Position, Altitude, Thrust, and P/Y/R Corrective Command Calculations
# noinspection SpellCheckingInspection
def calculate(n_position: object, n_target: object, n_alt: object,
              n_tgt_alt: object, n_THR: object, n_step: object) -> object:
    """

    :type n_step: object
    :type n_THR: object
    :type n_tgt_alt: object
    :type n_alt: object
    :type n_target: object
    :type n_position: object
    """
    global course, directory
    path: str = (directory + 'log/blackbox/CRS_DIR.iSr')
    virt_dist = n_target / 5
    vdb = virt_dist * 2
    vdc = virt_dist * 3
    vdd = virt_dist * 4
    if n_target > n_position:
        poscur: int = n_target - n_position
    elif n_target < n_position:
        poscur: int = n_position - n_target
    if poscur == n_target:
        n_position += 1
        course = False
    elif poscur < n_target:
        course = True
        n_position += 1
    elif poscur > n_target:
        course = True
        n_position -= 1
    if n_position < virt_dist:
        n_alt += virt_dist * 0.08
    elif virt_dist < n_position < vdb:
        n_alt += virt_dist * 0.16
    elif vdb < n_position < vdc:
        n_alt += 0
    elif n_position > vdc:
        n_alt -= virt_dist * 0.12
    # Throttle Control
    if ((n_position + 300) <= n_target) and (n_THR > 0):
        n_THR -= 1
    else:
        pass
    pct: str = str(
        "CPOS: " + str(n_position) + "  ID: " + str(poscur) + "  TGT: "
        + str(n_target) + "  CRS: " + str(course) + "  ALT: "
        + str(round(alt)) + "ft" + "  TGT ALT: " + str(n_tgt_alt)
        + "ft  " + "THR: " + str(THR))
    print(f'\r{pct}', end='')
    time.sleep(n_step)
    file_actions.writefile(pct, path)
    return n_position


# Hit confirmation output / define
def detonate(missile, alt, anti):
    """
    Detonation Command
    """
    explosive_mass = 300
    shrapnel = False
    if anti == 'yes':
        anti_tank: bool = True
    else:
        anti_tank = False
    warhead = "HEAT"
    print("Detonated. Explosive Mass of", explosive_mass, "Lbs Hit target successfully with",
          warhead, "warhead. ", "Shrapnel:",
          shrapnel, "  AT/AS:", anti_tank, "  Missile:", missile, "  Altitude:", alt)


def pitch(u_d, intgh, nr: object):
    """

    :type nr: object
    """
    if u_d == 'up':
        r = nr + intgh
        return r
    elif u_d == 'down':
        r = nr + intgh
        return r


def yaw(l_r, intgh, nr: object):
    """

    :type nr: object
    """
    if l_r == 'right':
        r = nr + intgh
        return r
    elif l_r == 'left':
        r = nr + intgh
        return r


def roll(l_r, intgh, nr: object):
    """

    :type nr: object
    """
    if l_r == 'right':
        r = nr + intgh
        return r
    elif l_r == 'left':
        r = nr + intgh
        return r

cpitch = 0
cyaw = 0
croll = 0
# On run
print('--------------------------------------')
print('   Missile Guidance System V2.7.1     ')
print(' [DSM 10] [PY 3.10] [WIN11] [DTR-45D] ')
print('--------------------------------------')
print(direct('/system'))
print()
stat()
info()
print(course(524, 216, 158))
# Design window
# Creating the Canvas
root = Tk()
# Title of the window
root.title("mgs_dev_1.0.0")
root.resizable(1, 1)
root.geometry("400x520")

# Button

b1 = Button(
    height=2, width=4,
    font=("Helvetica", "10"),
    text='Yaw \nLeft',
    foreground='green',
    command=yaw('left', 5, cyaw))
b1.grid(row=1, column=1)
b2 = Button(
    height=2, width=4,
    font=("Helvetica", "10"),
    text='Roll \nLeft',
    foreground='blue',
    command=roll('left', 5, croll))
b2.grid(row=2, column=1)
b3 = Button(
    height=2, width=4,
    font=("Helvetica", "10"),
    text='STAB \nAUG',
    foreground='orange',
    command='')
b3.grid(row=3, column=1)
b4 = Button(
    height=2, width=4,
    font=("Helvetica", "10"),
    text='Pitch \nDown',
    foreground='purple',
    command=pitch('down', 5, cpitch))
b4.grid(row=1, column=2)
b5 = Button(
    height=2, width=4,
    font=("Helvetica", "10"),
    text='CONF \nOK',
    foreground='red',
    command='')
b5.grid(row=2, column=2)
b6 = Button(
    height=2, width=4,
    font=("Helvetica", "10"),
    text='Pitch \nUp',
    foreground='purple',
    command=pitch('up', 5, cpitch))
b6.grid(row=3, column=2)
b7 = Button(
    height=2, width=4,
    font=("Helvetica", "10"),
    text='Yaw \nRight',
    foreground='green',
    command=yaw('right', 5, cyaw))
b7.grid(row=1, column=3)
b8 = Button(
    height=2, width=4,
    font=("Helvetica", "10"),
    text='Roll \nRight',
    foreground='blue',
    command=roll('right', 5, croll))
b8.grid(row=2, column=3)
b9 = Button(
    height=2, width=4,
    font=("Helvetica", "10"),
    text='RCS',
    foreground='orange',
    command='')
b9.grid(row=3, column=3)
"""t1 = Text(
    height=2, width=3,
    font=("Helvetica", "10"))
t1.grid(row=1, column=4)"""





mainloop()
