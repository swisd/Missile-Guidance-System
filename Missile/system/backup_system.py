"""backup_system.py"""
import Missile_Guidance_System as MGS
version = MGS.version
revision = MGS.revision
name = MGS.name
author = MGS.author
copyrightYear = MGS.copyright
mode = 'write'

if mode == 'write':
    filename = ("Missile/assets/back/" + name + "-" + revision + "-" + version + "--" + copyrightYear + "-" + author + ".bin")
    f = open(filename, "x")
    
if mode == 'read':
    pass
