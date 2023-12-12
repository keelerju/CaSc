from datetime import date, datetime
from random import choice
from caregivertype import CaregiverType
from assignablecaregiver import AssignableCaregiver
from skilltype import SkillType
from shift import Shift
from location import Location


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
    def initial_assignment(cls, rph_schedule, tech_schedule, team, weekend_rotation):
        """ Initial assignment of caregivers into the schedule."""
        
        rph_schedule = cls.assign_must_dates_rph(rph_schedule, team)
        tech_schedule = cls.assign_must_dates_tech(tech_schedule, team)

        rph_schedule = cls.assign_skilled_dates_rph(rph_schedule, team)

        rph_schedule = cls.assign_weekends_rph(rph_schedule, team, weekend_rotation)
        tech_schedule = cls.assign_weekends_tech(tech_schedule, team, weekend_rotation)

        rph_schedule = cls.create_initial_rph(rph_schedule, team)
        tech_schedule = cls.create_initial_tech(tech_schedule, team)

        return rph_schedule, tech_schedule

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
    def assign_skilled_dates_rph(cls, rph_schedule, team):
        """ Create a list of the rph_schedule indexes for shifts with skill requirements.
        Create a list of RPh caregivers with matching skill.
        Loop through the list of skilled shifts, and randomly assign a RPh caregiver to each shift.  """

        skilled_shift_indices = []
        for index, _shift in enumerate(rph_schedule):
            if SkillType.CHEMO in _shift.skills:
                skilled_shift_indices.append(index)

        skilled_rph = []
        for _caregiver in team:
            if (_caregiver.caregiver_type == CaregiverType.RPH) and (SkillType.CHEMO in _caregiver.skills):
                skilled_rph.append(_caregiver)

        for skilled_shift_index in skilled_shift_indices:
            rph_schedule[skilled_shift_index].caregiver_id_num = choice(skilled_rph).caregiver_id_num

        return rph_schedule

    @classmethod
    def assign_weekends_rph(cls, rph_schedule, team, weekend_rotation):
        
        weekend_difference = ((date(rph_schedule[0].year, rph_schedule[0].month, rph_schedule[0].day) - weekend_rotation.ref_date) - 1) / 7
        
        if weekend_difference > weekend_rotation.weekend_rph_count:
            weekend_difference %= weekend_rotation.weekend_rph_count
        
        if weekend_difference > 0:
            weekend_rph_index = weekend_rph_count - weekend_difference
        elif weekend_difference < 0:
            weekend_rph_index = weekend_rph_count + weekend_difference
        elif not weekend_difference:
            weekend_rph_index = 0
        
        for _shift in rph_schedule:
            if _shift.day_of_week == 1:
                _shift.caregiver_id_num = weekend_rotation.rph_schedule[weekend_rph_index].caregiver_id_number
            if _shift.day_of_week == 7:
                if weekend_rph_index < weekend_rph_count:
                    weekend_rph_index += 1
                else: 
                    weekend_rph_index = 0
                _shift.caregiver_id_num = weekend_rotation.rph_schedule[weekend_rph_index].caregiver_id_number
        
    @classmethod
    def assign_weekends_tech(cls, tech_schedule, team, weekend_rotation):
        pass

    @classmethod
    def create_initial_rph(cls, rph_schedule, team):
        """ Create assignable_team, a list of AssignableCaregiver objects, each having 2 attributes,
        the caregiver and the remaining hours yet to be assigned for them for that week.
        If the RPh works a number of hours per pay period that when divided in
        half is not divisible by the shift length (10 hours), then determine from a reference date in this method,
        which week of the pay period is being assigned, then apportion the shifts for that caregiver so that the
        first week, the remaining hours are rounded up to the nearest shift size, and the second week, the remaining
        hours are rounded down to the nearest shift size.
        Loop through the team and assign the correct number of remaining hours to each caregiver.
        Deduct the hours already assigned in that week of the RPh schedule from the remaining hours
        Randomly select an RPh caregiver, then randomly select a shift, and if RPh has remaining hours,
        and if there is no mismatch of skills, then assign the RPh to the shift. """

        rph_shift_length = 10
        extra_shifts = []
        reference_date_start_of_pay_period = datetime(2023, 12, 3)
        start_day = datetime(rph_schedule[0].year, rph_schedule[0].month, rph_schedule[0].day)
        week_difference = (start_day - reference_date_start_of_pay_period).days
        pay_period_week = 1
        if week_difference % 14 != 0:
            pay_period_week = 2
        for _week in range(1, rph_schedule[-1].week_of_month + 1):
            assignable_team = []
            for _caregiver in team:
                # skip per-diem RPh caregivers who have 0 minimum hours
                if _caregiver.min_hours == 0:
                    continue
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
            # to the RPh schedule.  If there are remaining RPh caregivers after exhausting available shifts,
            # random shifts will be added to the list extra_shifts, which is added back to rph_schedule finally.
            while total_remaining_hours:
                assignee = choice(assignable_team)
                shift_assignment = choice(range(((_week - 1) * shift_count), ((_week * shift_count) + 1)))
                if (not rph_schedule[shift_assignment].caregiver_id_num and (assignee.remaining_hours != 0)
                        and cls.skills_no_mismatch(assignee.caregiver, rph_schedule[shift_assignment])
                        and (date(rph_schedule[shift_assignment].year, rph_schedule[shift_assignment].month,
                                  rph_schedule[shift_assignment].day) not in assignee.caregiver.cant_dates)):
                    rph_schedule[shift_assignment].caregiver_id_num = assignee.caregiver.caregiver_id_num
                    assignee.remaining_hours -= rph_shift_length
                    shift_count -= 1
                    if assignee.remaining_hours == 0:
                        assignable_team.remove(assignee)
                    for assignee in assignable_team:
                        total_remaining_hours += assignee.caregiver.remaining_hours
                    if total_remaining_hours and not shift_count:
                        for _assignee in assignable_team:
                            random_day = choice([2, 3, 4, 5, 6])
                            random_location = choice([Location.INPATIENT, Location.RETAIL])
                            random_day_start = choice([7, 7.5])
                            extra_shifts.append(Shift(day_of_week=random_day, location=random_location,
                                                      start_time=random_day_start, end_time=(random_day_start + 10.5),
                                                      caregiver_type=CaregiverType.RPH, skills=set()))
            pay_period_week = 2 if pay_period_week == 1 else 1
        for extra_shift in extra_shifts:
            rph_schedule.append(extra_shift)
        return rph_schedule

    @classmethod
    def create_initial_tech(cls, tech_schedule, team):
        pass

    def refinement(self, rph_schedule, tech_schedule, team, evaluation):
        pass
