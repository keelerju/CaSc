from enum import Enum


class SkillType(Enum):
    """ Skill implies caregiver can work independently with this skill """
    CHEMO = 1
    RETAIL = 2
    INPATIENT = 3
