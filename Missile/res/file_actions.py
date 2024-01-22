"""File Actions"""

def writefile(data: object, location: object) -> object:
    """

    :rtype: object
    :param data: 
    :param location: 
    """
    f = open(location, "a")
    f.write(data)
    f.write('')
    f.close()

def writeFileNoAppend(data: object, location: object) -> object:
    """

    :rtype: object
    :param data:
    :param location:
    """
    f = open(location, "w")
    f.write(data)
    f.write('')
    f.close()
