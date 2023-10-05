#Missile Guidance System.py


from LNmain import LNRmain as LNR
import time
import corrective_commands
import file_actions
import math

virt_alt = 1
valueError = "Error. Impossible values."
pitch = 0
roll = 0
yaw = 0
alt = 0
spd = 0
thr = 0
ws = [0, 0]
atp = 14.7  # ASL
eng_ves_a = 0
eng_vec_b = 0
position = int(input("Start POS: "))
target = int(input("TGT POS: "))
tgt_alt = int(input("TGT ALT: "))
anti: str = str(input("AT/AS: "))
step = float(input("TS: "))
missile: str = str(input("Type: "))


def stat():
    arc = 'MSL_PROG'
    curve = 'normal-UUFD'
    method = 'High Top Drop'
    path = [52, 85, 0, -65]
    print("ARC: " + arc + "  Curve: " + curve + "  Method: " + method + "  PATH: " + str(path))


def course():
    pass

def info():
    print("CPU Cores:", LNR.cpu_count(), "  CPU Type:", "11th Gen Intel(R) Core(TM) i7-1185G7 @ 3.00 GHz", "  VT:", LNR._VT, "  CPU Temp:", "N/A")
    print("GPU Cores:", "N/A", "  GPU Type:", "Intel(R) Iris(R) Xe Graphics", "  VT:", LNR._KT_co, "  GPU Temp:", "N/A")


virt_dist = target / 5
vdb = virt_dist * 2
vdc = virt_dist * 3
vdd = virt_dist * 4
stat()
info()

thr: int = corrective_commands.Command.goToTHR_UPDN(corrective_commands.Command.command('SLF', 'cmd'), thr, 100, thr)
#DPS, Position, Altitude, Thrust, and P/Y/R Corrective Command Calculations

while position != target and alt != tgt_alt:
    if target > position:
        poscur: int = target - position

    elif target < position:
        poscur: int = position - target

    if poscur == target:
        position: int = position + 1
        course: bool = False

    elif poscur < target:
        course: bool = True
        position: int = position + 1

    elif poscur > target:
        course: bool = True
        position: int = position - 1

    if position < virt_dist:
        alt = alt + virt_dist * 0.08
    elif position > virt_dist and position < vdb:
        alt = alt + virt_dist * 0.16
    elif position > vdb and position < vdc:
        alt = alt + 0
    elif position > vdc:
        alt = alt - virt_dist * 0.12
    pct: str = str("CPOS: " + str(position) + "  ID: " + str(poscur) + "  TGT: " + str(target) + "  CRS: " + str(course)
                   + "  ALT: " + str(round(alt)) + "ft" + "  TGT ALT: " + str(tgt_alt) + "ft  " + "THR: " + str(thr))
    print(f'\r{pct}', end='')
    time.sleep(step)
    file_actions.writefile(pct, 'C:\PyDev\Missile\CRS_DIR.iSr')

#Hit confirmation output / define

def error():
    print(valueError)

def detonate():
    explosivemass = 30
    shrapnel = False
    if anti == 'yes':
        antiTank = True
    else:
        antiTank = False
    warhead = "HEAT"
    print("Detonated. Explosive Mass of", explosivemass, "Lbs Hit target successfully with", warhead, "warhead. "
                                                                                                      "Shrapnel:",
          shrapnel, "  AT/AS:", antiTank, "  Missile:", missile, "  Altitude:", tgt_alt)


missilePosition = position
missileTarget = target

if missilePosition != missileTarget:
    error()


if position == target:
    print(position, poscur, target, "Hit")
    time.sleep(0.1)
    detonate()

print(missilePosition, missileTarget)
