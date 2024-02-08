"""Missile Guidance System (Main)"""
# Missile Guidance System.py
# noinspection PylintInspection
import math
import os
import platform
import time
from Missile.res import corrective_commands, file_actions, ns_cwd, define
from Missile.guidance import data_injector

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
# Inputs
print('--------------------------------------')
print('   Missile Guidance System V2.7.1     ')
print(' [DSM 10] [PY 3.10] [WIN11] [DTR-45D] ')
print('--------------------------------------')
position = int(input("Start POS: "))
target = int(input("TGT POS: "))
tgt_alt = int(input("TGT ALT: "))
anti: str = str(input("AT/AS: "))
step = float(input("TS: "))
print(missile_list)
missile: str = str(input("Type: "))
print('--------------------------------------')

VERSION = '2.7.1'
REVISION = 'MSL-GUID-REV2'
NAME = 'Missile Guidance System'
AUTHOR = 'swisd'
COPYRIGHT = '2024'


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


# fDIR = str(os.getcwd()) + '/log/blackbox/CRS_DIR.iSr'

virt_dist = target / 5
vdb = virt_dist * 2
vdc = virt_dist * 3
vdd = virt_dist * 4

print(direct())
print()
stat()
info()

print(course(524, 216, 158))

THR: int = 100
# DPS, Position, Altitude, Thrust, and P/Y/R Corrective Command Calculations
# noinspection SpellCheckingInspection

while position != target and alt != tgt_alt:
    if target > position:
        poscur: int = target - position
    elif target < position:
        poscur: int = position - target
    if poscur == target:
        position += 1
        course: bool = False
    elif poscur < target:
        course: bool = True
        position += 1
    elif poscur > target:
        course: bool = True
        position -= 1
    if position < virt_dist:
        alt += virt_dist * 0.08
    elif virt_dist < position < vdb:
        alt += virt_dist * 0.16
    elif vdb < position < vdc:
        alt += 0
    elif position > vdc:
        alt -= virt_dist * 0.12
    # Throttle Control
    if ((position + 300) <= target) and (THR > 0):
        THR -= 1
    else:
        pass
    pct: str = str(
        "CPOS: " + str(position) + "  ID: " + str(poscur) + "  TGT: "
        + str(target) + "  CRS: " + str(course) + "  ALT: "
        + str(round(alt)) + "ft" + "  TGT ALT: " + str(tgt_alt)
        + "ft  " + "THR: " + str(THR))
    print(f'\r{pct}', end='')
    time.sleep(step)
    file_actions.writefile(pct, 'C:/PyDev/Missile/log/blackbox')


# Hit confirmation output / define

def error():
    """
    Value Error
    """
    print(valueError)


def detonate():
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


missilePosition = position
missileTarget = target

if missilePosition != missileTarget:
    error()

if position == target:
    print(position, poscur, target, "Hit")
    time.sleep(0.1)
    detonate()
dps = missilePosition / missileTarget * 2

print(missilePosition, missileTarget, math.sqrt(dps))

dataClear: str = input('Clear Data? (Y/N)')
if dataClear == 'Y':
    data_injector.clear_dir()
    data_injector.clear_corr()
else:
    pass

print('Missile Guidance System MSL-GUID-REV2-V2.7.1')
