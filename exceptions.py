class Error(Exception):
    """Base class for other exceptions"""
    pass


class BadValue(Error):
    """Bad input value"""
    pass


class DoubledValue(Error):
    """Doubled value"""
    pass