"""File Actions"""

def writefile(data: object, location: object) -> object:
    """

    :rtype: object
    :param data: 
    :param location: 
    """
    _f = open(location, "a")
    _f.write(data)
    _f.write('')
    _f.close()

def writeFileNoAppend(data: object, location: object) -> object:
    """

    :rtype: object
    :param data:
    :param location:
    """
    _f = open(location, "w")
    _f.write(data)
    _f.write('')
    _f.close()
