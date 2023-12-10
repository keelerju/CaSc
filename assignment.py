from datetime import date, datetime
from random import choice
from caregivertype import CaregiverType


class Assignment:
    """ Class with class methods that accept schedules, team, and evaluation objects, that assigns caregivers
    initially and employs various strategies for refinement based on evaluation criteria """

    def __init__(self):
        pass

    @classmethod
    def skills_no_mismatch(cls, _caregiver, _shift):
        """ Return true if a shift skill requirement matches a caregiver skill """
        for _caregiver_skill in _caregiver.skills:
            for _shift_skill in _shift.skills:
                if _shift_skill == _caregiver_skill:
                    return True
        return False

    @classmethod
    def initial_assignment(cls, rph_schedule, rph_template, tech_schedule, tech_template, team):
        """ Initial assignment of caregivers into the schedule."""

        # Go through each caregiver, and if RPh, find their must-dates, if any, and
        # randomly assign them a shift on those dates. If no available shifts, provide a warning.
        for _caregiver in team.team:
            if _caregiver.must_dates and (_caregiver.caregiver_type == CaregiverType.RPH):
                for _date in _caregiver.must_dates:
                    _shifts = []
                    for index, _shift in enumerate(rph_schedule):
                        if ((_date == date(_shift.year, _shift.month, _shift.day_of_month))
                                and not _shift.caregiver_id_num and cls.skills_no_mismatch(_caregiver, _shift)):
                            _shifts.append((index, _shift))
                    if not _shifts:
                        print(f"Cannot assign caregiver with ID# {_caregiver.caregiver_id_num} to "
                              f"any shift on {_date} because of no available shifts.")
                        break
                    else:
                        chosen_shift = choice(_shifts)
                        rph_schedule[_shifts[0]].caregiver_id_num = chosen_shift[1].caregiver_id_num

        # Go through each caregiver, and if Tech, find their must-dates, if any, and
        # randomly assign them a shift on those dates. If no available shifts, provide a warning.
        for _caregiver in team.team:
            if _caregiver.must_dates and (_caregiver.caregiver_type == CaregiverType.TECH):
                for _date in _caregiver.must_dates:
                    _shifts = []
                    for index, _shift in enumerate(tech_schedule):
                        if ((_date == date(_shift.year, _shift.month, _shift.day_of_month))
                                and not _shift.caregiver_id_num and cls.skills_no_mismatch(_caregiver, _shift)):
                            _shifts.append((index, _shift))
                    if not _shifts:
                        print(f"Cannot assign caregiver with ID# {_caregiver.caregiver_id_num} to "
                              f"any shift on {_date} because of no available shifts.")
                        break
                    else:
                        chosen_shift = choice(_shifts)
                        tech_schedule[_shifts[0]].caregiver_id_num = chosen_shift[1].caregiver_id_num

        # Create local_team, a list of objects each with 2 attributes, the caregiver and the remaining hours
        # yet to be assigned for them for that week. 
        # If the RPh works a number of hours per pay period that when divided in
        # half is not divisible by the shift length (10 hours), then determine from a reference date in this method,
        # which week of the pay period is being assigned, then apportion the shifts for that caregiver so that the
        # first week, the remaining hours are rounded up to the nearest shift size, and the second week, the remaining
        # hours are rounded down to the nearest shift size.
        # Loop through the team and assign the correct number of remaining hours to each tuple. 
        # Deduct the hours already assigned in that week of the RPh schedule from the remaining hours
        # Randomly select an RPh caregiver from then randomly select a shift, and if RPh has remaining hours,
        # and if there is no mismatch of skills, then assign the RPh to the shift.

        local_team = []
        reference_date_start_of_pay_period = datetime(2023, 12, 3)
        start_day = datetime(rph_schedule[0].year, rph_schedule[0].month, rph_schedule[0].day)
        week_difference = (start_day - reference_date_start_of_pay_period).days
        pay_period_week = 1
        if week_difference % 14 != 0:
            pay_period_week = 2

        # Do the same for the Techs as above.

    def refinement(self, rph_schedule, tech_schedule, team, evaluation):
        pass
