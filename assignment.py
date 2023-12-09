from datetime import date
from random import choice
from caregivertype import CaregiverType


class Assignment:
    """ Class with class methods that accept schedules, team, and evaluation objects, that assigns caregivers
    initially and employs various strategies for refinement based on evaluation criteria """

    def __init__(self):
        pass

    @classmethod
    def attribute_no_mismatch(cls, _caregiver, _shift):
        """ Return true if a shift requirement matches a caregiver attribute """
        for attribute in _caregiver.attributes:
            for _special_req in _shift.special_reqs:
                if _special_req == attribute:
                    return True
        return False

    @classmethod
    def initial_assignment(cls, rph_schedule, tech_schedule, team, evaluation):
        """ Go through each caregiver, find their must-dates, if any, and
        randomly assign them a shift on those dates. If no available shifts, provide a warning. """
        for _caregiver in team.team:
            if _caregiver.must_dates and (_caregiver.caregiver_type == CaregiverType.RPH):
                for _date in _caregiver.must_dates:
                    _shifts = []
                    for index, _shift in enumerate(rph_schedule):
                        if ((_date == date(_shift.year, _shift.month, _shift.day_of_month))
                                and not _shift.caregiver_id_num and cls.attribute_no_mismatch(_caregiver, _shift)):
                            _shifts.append((index, _shift))
                    if not _shifts:
                        print(f"Cannot assign caregiver with ID# {_caregiver.caregiver_id_num} to "
                              f"any shift on {_date} because of no available shifts.")
                        break
                    else:
                        chosen_shift = choice(_shifts)
                        rph_schedule[_shifts[0]].caregiver_id_num = chosen_shift[1].caregiver_id_num

        for _caregiver in team.team:
            if _caregiver.must_dates and (_caregiver.caregiver_type == CaregiverType.TECH):
                for _date in _caregiver.must_dates:
                    _shifts = []
                    for index, _shift in enumerate(tech_schedule):
                        if ((_date == date(_shift.year, _shift.month, _shift.day_of_month))
                                and not _shift.caregiver_id_num and cls.attribute_no_mismatch(_caregiver, _shift)):
                            _shifts.append((index, _shift))
                    if not _shifts:
                        print(f"Cannot assign caregiver with ID# {_caregiver.caregiver_id_num} to "
                              f"any shift on {_date} because of no available shifts.")
                        break
                    else:
                        chosen_shift = choice(_shifts)
                        tech_schedule[_shifts[0]].caregiver_id_num = chosen_shift[1].caregiver_id_num

    def refinement(self, rph_schedule, tech_schedule, team, evaluation):
        pass
