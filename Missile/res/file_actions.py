"""File Actions"""


def writefile(data: object, location: object) -> object:
    """

    :rtype: object
    :param data:
    :param location:
    """
    with open(location, "a", encoding="utf-8") as _f:
        _f.write(data)
        _f.write('')
        _f.close()


def writeFileNoAppend(data: object, location: object) -> object:
    """

    :rtype: object
    :param data:
    :param location:
    """
    with open(location, "w", encoding="utf-8") as _f:
        _f.write(data)
        _f.write('')
        _f.close()
