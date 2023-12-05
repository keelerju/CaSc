from enum import Enum


class ConsCritType(Enum):
    """ Class representing the type of constraint criteria """

    NONE = 0
    MUST_WORK = 1
    CANT_WORK = 2
