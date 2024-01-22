"""backup_system.py"""
import Missile_Guidance_System as MGS
VERSION = MGS.VERSION
REVISION = MGS.REVISION
NAME = MGS.NAME
AUTHOR = MGS.AUTHOR
COPYRIGHTYEAR = MGS.COPYRIGHT
MODE = 'write'

if MODE == 'write':
    FILENAME = ("Missile/assets/back/" + NAME + "-" + REVISION + "-" + VERSION
        + "--" + COPYRIGHTYEAR + "-" + AUTHOR + ".bin")
    f = open(FILENAME, "x")
if MODE == 'read':
    pass
