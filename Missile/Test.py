"""Testing File"""
import os
from Missile.res import corrective_commands
print(corrective_commands.Command.go_to_thr(corrective_commands.Command.command('command', 'cmd[x]'), 4, 100, 4))

print("Current Working Directory " , str(os.getcwd()))
print("Current File Directory " , str(os.getcwd()) + "/system")
