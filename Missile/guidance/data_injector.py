"""Data Injector Program"""

from Missile.res import file_actions


def inject_data(data, location, position):
    """Insert Data"""
    file_actions.writefile(str(data), location)
    return position


def clear_corr():
    """Clear CORR Log"""
    file_actions.writeFileNoAppend('*dsp//CRS_CORR.iSr,  CMD/DATA?rS CMD -LOG->',
                                   'C:/PyDev/Missile/log/blackbox/CRS_CORR.iSr')


def clear_dir():
    """Clear DIR Log"""
    file_actions.writeFileNoAppend('*dsp//CRS_DIR.iSr,  CMD/DATA?rS CMD -LOG->',
                                   'C:/PyDev/Missile/log/blackbox/CRS_DIR.iSr')
