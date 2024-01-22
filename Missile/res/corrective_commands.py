#corrective_commands.py
"""Corrective Guidance Commands"""
class Command():
    """Corrective Commands"""

    def command(self, cmd: object = str) -> object:
     """

     :param cmd:
     :return:
     """
     return str(cmd)
     pass

    def goToPos(self, cpos_x: object, cpos_y: object, cpos_z: object, pitch: object, yaw: object, roll: object, pos_x: object, pos_y: object, pos_z: object) -> object:
        """

        :rtype: object
        :param cpos_x:
        :param cpos_y:
        :param cpos_z:
        :param pitch:
        :param yaw:
        :param roll:
        :param pos_x:
        :param pos_y:
        :param pos_z:
        """
        pass

    def goToTHR_UPDN(self, Tc: object, Tt: object, Tcur: object) -> object:
          """

          :rtype: object
          """
          Tc = Tc + Tt - Tc
          return Tc
    pass

    def __RTG_KT_CO_VT_DP__(self, vt: object, vr: object, ac: object, ) -> object:
        """

        :rtype: object
        :param vt:
        :param vr:
        :param ac:
        """
        pass

class Action():
    pass
