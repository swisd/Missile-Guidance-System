#test.py
from Missile.res import corrective_commands

print(corrective_commands.Command.goToTHR_UPDN(corrective_commands.Command.command('command', 'cmd[x]'), 4, 100, 4))

