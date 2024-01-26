"""backup_system.py"""
import missile_guidance_system_main as MGS

VERSION = MGS.VERSION
REVISION = MGS.REVISION
NAME = MGS.NAME
AUTHOR = MGS.AUTHOR
COPYRIGHTYEAR = MGS.COPYRIGHT
MODE = 'write'

if MODE == 'write':
    FILENAME = ("Missile/assets/back/" + NAME + "-" + REVISION + "-" + VERSION
                + "--" + COPYRIGHTYEAR + "-" + AUTHOR + ".bin")
    with open(FILENAME, "x", encoding="utf-8") as f:
        pass
if MODE == 'read':
    pass
