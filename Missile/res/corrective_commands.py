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
    def go_to_pos(self, cpos_x: object, cpos_y: object, cpos_z: object, pitch: object, yaw: object, roll: object, pos_x: object, pos_y: object, pos_z: object) -> object:
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


    def go_to_thr(self, t_c: object, t_t: object, t_cur: object) -> object:
        """

        :rtype: object
        """
        t_c = t_c + (t_t - t_c) - t_cur
        return t_c,


    def __RTG_KT_CO_VT_DP__(self, v_t: object, v_r: object, a_c: object, ) -> object:
        """

        :rtype: object
        :param v_t:
        :param v_r:
        :param a_c:
        """

class Action():
    """Control Actions"""
    def pitch(self):
        """Pitch Control"""

    def roll(self):
        """Roll Control"""

    def yaw(self):
        """Yaw Control"""
