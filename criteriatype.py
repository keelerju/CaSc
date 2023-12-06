from enum import Enum


class CriteriaType(Enum):
    """ Class representing the type of constraint criteria """

    NONE = 0
    CANT_WORK = 1
    MUST_WORK = 2
    CHEMO_MIXER = 3
