"""File Actions"""


def writefile(data: object, location: object) -> object:
    """

    :rtype: object
    :param data:
    :param location:
    """
    with open(location, "a", encoding="utf-8") as _f:
        _f.write(str(data))
        _f.close()


def write_file_no_append(ud_data: object, location: object) -> object:
    """

    :rtype: object
    :param data:
    :param location:
    """
    with open(location, "w", encoding="utf-8") as _f:
        _f.write(str(ud_data))
        _f.write('')
        _f.close()
