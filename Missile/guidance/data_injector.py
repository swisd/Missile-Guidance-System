"""Data Injector Program"""

from Missile.res import file_actions

REPLACE_TXT = '*dsp//CRS_CORR.iSr,  CMD/DATA?rS CMD -LOG->'


def inject_data(data, location, position):
    """Insert Data"""
    file_actions.writefile(str(data), location)
    return position


def clear_corr():
    """Clear CORR Log"""
    file_actions.writeFileNoAppend(REPLACE_TXT,
                                   'C:/PyDev/Missile/log/blackbox/CRS_CORR.iSr')


def clear_dir():
    """Clear DIR Log"""
    file_actions.writeFileNoAppend(REPLACE_TXT,
                                   'C:/PyDev/Missile/log/blackbox/CRS_DIR.iSr')
