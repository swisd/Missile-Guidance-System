'Data Injector Program'

from Missile.res import file_actions
import time


def injectData(data, location, position):
	file_actions.writefile(str(data), location)


def clearCORR():
	file_actions.writeFileNoAppend('*dsp//CRS_CORR.iSr,  CMD/DATA?rS CMD -LOG->',
								   'C:/PyDev/Missile/log/blackbox/CRS_CORR.iSr')


def clearDIR():
	file_actions.writeFileNoAppend('*dsp//CRS_DIR.iSr,  CMD/DATA?rS CMD -LOG->',
								   'C:/PyDev/Missile/log/blackbox/CRS_DIR.iSr')
