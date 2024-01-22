'Data Injector Program'

from Missile.res import file_actions


def injectData(data, location, position):
    """Insert Data"""
    file_actions.writefile(str(data), location)
    return position


def clearCORR():
    """Clear CORR Log"""
    file_actions.writeFileNoAppend('*dsp//CRS_CORR.iSr,  CMD/DATA?rS CMD -LOG->',
                                   'C:/PyDev/Missile/log/blackbox/CRS_CORR.iSr')


def clearDIR():
    """Clear DIR Log"""
    file_actions.writeFileNoAppend('*dsp//CRS_DIR.iSr,  CMD/DATA?rS CMD -LOG->',
                                   'C:/PyDev/Missile/log/blackbox/CRS_DIR.iSr')
