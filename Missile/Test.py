#test.py
import time
import math

pitch = 0
roll = 0
yaw = 0
alt = 0
spd = 0
thr = 0
ws = [0,0]
atp = 14.7 #ASL
position = int(input("Start POS: "))
target = int(input("TGT POS: "))
anti:str = str(input("AT/AS: "))
step = float(input("TS: "))
missile: str = str(input("Type:"))

while position != target:
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
 pct:str = str("CPOS: " + str(position) + "  ID: " + str(poscur) + "  TGT: " + str(target) + "  CRS: " + str(course))
 print(f'\r{pct}', end='')
 time.sleep(step)

