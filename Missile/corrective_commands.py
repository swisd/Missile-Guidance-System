#corrective_commands.py

import math
import time

class Command():

    def command(self, cmd=str):
     return str(cmd)
     pass

    def goToPos(self, cpos_x, cpos_y, cpos_z, pitch, yaw, roll, pos_x, pos_y, pos_z):
        pass

    def goToTHR_UPDN(self, Tc, Tt, Tcur):
          Tc = Tc + Tt - Tc
          return Tc
    pass

class Action():
    pass
