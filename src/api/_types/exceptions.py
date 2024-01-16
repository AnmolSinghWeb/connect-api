
class NtException(Exception):
    """Generic NT exceptions"""

class NtUnkownData(NtException):
    """When data passed is unkown"""

class NtNotImplemented(NtException):
    """When a class interface is not imprlemented"""

class NtReadOnlyField(NtException):
    """
        When someone or something try to change the values
        of a variable that must not be changed
    """
