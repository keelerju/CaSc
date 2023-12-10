from datetime import date, datetime
from random import choice
from caregivertype import CaregiverType
from assignablecaregiver import AssignableCaregiver


class Assignment:
    """ Class with class methods that accept schedules, team, and evaluation objects, that assigns caregivers
    initially and employs various strategies for refinement based on evaluation criteria """

    def __init__(self):
        pass

    @classmethod
    def skills_no_mismatch(cls, _caregiver, _shift):
        """ Return true if there is no mismatch between a shift skill requirement and a caregiver skill """
        if not _shift.skills:
            return True
        elif not _caregiver.skills:
            return False
        for _caregiver_skill in _caregiver.skills:
            for _shift_skill in _shift.skills:
                if _shift_skill == _caregiver_skill:
                    return True
        return False

    @classmethod
    def initial_assignment(cls, rph_schedule, tech_schedule, team):
        """ Initial assignment of caregivers into the schedule."""
        
        rph_schedule = cls.assign_must_dates_rph(rph_schedule, tech_schedule)
        tech_schedule = cls.assign_must_dates_tech(tech_schedule, tech_schedule)
        
        rph_schedule = cls.create_initial_rph(rph_schedule, team)
        tech_schedule = cls.create_initial_tech(tech_schedule, team)

    @classmethod
    def assign_must_dates_rph(cls, rph_schedule, team):
        """ Loop through each caregiver, and if RPh, find their must-dates, if any, and
        randomly assign them a shift on those dates. If no available shifts, provide a warning. """

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
        return rph_schedule
    
    @classmethod
    def assign_must_dates_tech(cls, tech_schedule, team):
        """ Loop through each caregiver, and if Tech, find their must-dates, if any, and
        randomly assign them a shift on those dates. If no available shifts, provide a warning. """
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
        return tech_schedule
    
    @classmethod
    def create_initial_rph(cls, rph_schedule, team):
        """ Create assignable_team, a list of objects each with 2 attributes, the caregiver and the remaining hours
        yet to be assigned for them for that week. 
        If the RPh works a number of hours per pay period that when divided in
        half is not divisible by the shift length (10 hours), then determine from a reference date in this method,
        which week of the pay period is being assigned, then apportion the shifts for that caregiver so that the
        first week, the remaining hours are rounded up to the nearest shift size, and the second week, the remaining
        hours are rounded down to the nearest shift size.
        Loop through the team and assign the correct number of remaining hours to each tuple. 
        Deduct the hours already assigned in that week of the RPh schedule from the remaining hours
        Randomly select an RPh caregiver, then randomly select a shift, and if RPh has remaining hours,
        and if there is no mismatch of skills, then assign the RPh to the shift. """

        rph_shift_length = 10
        reference_date_start_of_pay_period = datetime(2023, 12, 3)
        start_day = datetime(rph_schedule[0].year, rph_schedule[0].month, rph_schedule[0].day)
        week_difference = (start_day - reference_date_start_of_pay_period).days
        pay_period_week = 1
        if week_difference % 14 != 0:
            pay_period_week = 2
        for _week in range(1, rph_schedule[-1].week_of_month + 1):
            assignable_team = []
            for _caregiver in team:
                remaining_hours = _caregiver.min_hours / 2
                if remaining_hours % rph_shift_length != 0:
                    if pay_period_week == 1:
                        remaining_hours += (rph_shift_length / 2)
                    elif pay_period_week == 2:
                        remaining_hours -= (rph_shift_length / 2)
                assignable_team.append(AssignableCaregiver(_caregiver, remaining_hours))

            # provide a count of shifts in this week
            shift_count = 0
            for _shift in rph_schedule:
                if _shift.week_of_month == _week:
                    shift_count += 1

            # provide a count of remaining hours for the entire assignable team in this week
            total_remaining_hours = 0
            for assignee in assignable_team:
                total_remaining_hours += assignee.caregiver.remaining_hours

            # As long as there are remaining hours amongst the assignable team, randomly try to assign a caregiver
            # to the RPh schedule.  (possible infinite loop - needs debugging to find all failure cases)
            # Foresee that these failure cases include at least:
            #     1: no remaining caregivers who have the skills for the remaining shift(s).
            #     2: too many caregivers for the available shifts, so need to be able to create extra shifts in the
            #        schedule that are strategically placed based on heaviest need.
            while total_remaining_hours:
                assignee = choice(assignable_team)
                shift_assignment = choice(range(((_week - 1) * shift_count), ((_week * shift_count) + 1)))
                if (not rph_schedule[shift_assignment].caregiver_id_num and (assignee.remaining_hours != 0)
                        and cls.skills_no_mismatch(assignee.caregiver, rph_schedule[shift_assignment])):
                    rph_schedule[shift_assignment].caregiver_id_num = assignee.caregiver.caregiver_id_num
                    assignee.remaining_hours -= rph_shift_length
                    total_remaining_hours -= rph_shift_length
                
            pay_period_week = 2 if pay_period_week == 1 else 1
        return rph_schedule

    @classmethod
    def create_initial_tech(cls, tech_schedule, team):
        pass

    def refinement(self, rph_schedule, tech_schedule, team, evaluation):
        pass
