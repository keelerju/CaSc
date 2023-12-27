from datetime import date, datetime, timedelta
from random import choice
from caregivertype import CaregiverType
from assignablecaregiver import AssignableCaregiver
from skilltype import SkillType
from shift import Shift
from location import Location


class Assignment:
    """ Class with methods that accept schedules, team, weekend rotation, and evaluation objects, that
        assigns caregivers initially and employs various strategies for refinement based on evaluation criteria """

    def __init__(self, rph_schedule, tech_schedule, team, weekend_rotation, evaluation):
        self.rph_schedule = rph_schedule
        self.tech_schedule = tech_schedule
        self.team = team
        self.weekend_rotation = weekend_rotation
        self.evaluation = evaluation

        self.initial_assignment()

    @staticmethod
    def skills_no_mismatch(_caregiver, _shift):
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

    def initial_assignment(self):
        """ Initial assignment of caregivers into the schedule."""
        
        self.assign_must_dates_rph()
        self.assign_must_dates_tech()

        self.assign_skilled_dates_rph()

        self.assign_weekends_rph()
        self.assign_weekends_tech()

        self.assign_cant_dates_rph()
        self.assign_cant_dates_tech()

        self.rph_schedule = self.create_initial(self.rph_schedule, 10, CaregiverType.RPH)
        self.tech_schedule = self.create_initial(self.tech_schedule, 8, CaregiverType.TECH)

    def assign_must_dates_rph(self):
        """ Loop through each caregiver, and if RPh, find their must-dates, if any, and
            randomly assign them a shift on those dates. If no available shifts, provide a warning. """

        for _caregiver in self.team:
            if _caregiver.must_dates and (_caregiver.caregiver_type == CaregiverType.RPH):
                for _date in _caregiver.must_dates:
                    _shifts = []
                    for index, _shift in enumerate(self.rph_schedule):
                        if ((_date == date(_shift.year, _shift.month, _shift.day_of_month))
                                and not _shift.caregiver_id_num and self.skills_no_mismatch(_caregiver, _shift)):
                            _shifts.append((index, _shift))
                    if not _shifts:
                        print(f"Cannot assign caregiver with ID# {_caregiver.caregiver_id_num} to "
                              f"any shift on {_date} because of no available shifts.")
                        break
                    else:
                        chosen_shift = choice(_shifts)
                        self.rph_schedule[_shifts[0]].caregiver_id_num = chosen_shift[1].caregiver_id_num

    def assign_must_dates_tech(self):
        """ Loop through each caregiver, and if Tech, find their must-dates, if any, and
            randomly assign them a shift on those dates. If no available shifts, provide a warning. """
        
        for _caregiver in self.team:
            if _caregiver.must_dates and (_caregiver.caregiver_type == CaregiverType.TECH):
                for _date in _caregiver.must_dates:
                    _shifts = []
                    for index, _shift in enumerate(self.tech_schedule):
                        if ((_date == date(_shift.year, _shift.month, _shift.day_of_month))
                                and not _shift.caregiver_id_num and self.skills_no_mismatch(_caregiver, _shift)):
                            _shifts.append((index, _shift))
                    if not _shifts:
                        print(f"Cannot assign caregiver with ID# {_caregiver.caregiver_id_num} to "
                              f"any shift on {_date} because of no available shifts.")
                        break
                    else:
                        chosen_shift = choice(_shifts)
                        self.tech_schedule[_shifts[0]].caregiver_id_num = chosen_shift[1].caregiver_id_num

    def assign_skilled_dates_rph(self):
        """ Create a list of the rph_schedule indexes for shifts with skill requirements.
            Create a list of RPh caregivers with matching skill.
            Loop through the list of skilled shifts, and randomly assign a RPh caregiver to each shift.  """

        skilled_shift_indices = []
        for index, _shift in enumerate(self.rph_schedule):
            if SkillType.CHEMO in _shift.skills:
                skilled_shift_indices.append(index)

        skilled_rph = []
        for _caregiver in self.team:
            if (_caregiver.caregiver_type == CaregiverType.RPH) and (SkillType.CHEMO in _caregiver.skills):
                skilled_rph.append(_caregiver)

        for skilled_shift_index in skilled_shift_indices:
            self.rph_schedule[skilled_shift_index].caregiver_id_num = choice(skilled_rph).caregiver_id_num

    def assign_weekends_rph(self):
        
        weekend_difference = ((date(self.rph_schedule[0].year, self.rph_schedule[0].month,
                                    self.rph_schedule[0].day) - self.weekend_rotation.ref_date_rph) - 1) / 7
        weekend_rph_index = 0

        if weekend_difference > self.weekend_rotation.weekend_rph_count:
            weekend_difference %= self.weekend_rotation.weekend_rph_count
        
        if weekend_difference > 0:
            weekend_rph_index = self.weekend_rotation.weekend_rph_count - weekend_difference
        elif weekend_difference < 0:
            weekend_rph_index = self.weekend_rotation.weekend_rph_count + weekend_difference
        elif not weekend_difference:
            weekend_rph_index = 0
        
        for _shift in self.rph_schedule:
            if _shift.day_of_week == 1:
                _shift.caregiver_id_num = self.weekend_rotation.rph_schedule[weekend_rph_index].caregiver_id_number
            if _shift.day_of_week == 7:
                if weekend_rph_index < self.weekend_rotation.weekend_rph_count:
                    weekend_rph_index += 1
                else: 
                    weekend_rph_index = 0
                _shift.caregiver_id_num = self.weekend_rotation.rph_schedule[weekend_rph_index].caregiver_id_number

    def assign_weekends_tech(self):

        weekend_difference = ((date(self.tech_schedule[0].year, self.tech_schedule[0].month,
                                    self.tech_schedule[0].day) - self.weekend_rotation.ref_date_tech) - 1) / 7
        weekend_tech_index = 0

        if weekend_difference > self.weekend_rotation.weekend_tech_count:
            weekend_difference %= self.weekend_rotation.weekend_tech_count

        if weekend_difference > 0:
            weekend_tech_index = self.weekend_rotation.weekend_tech_count - weekend_difference
        elif weekend_difference < 0:
            weekend_tech_index = self.weekend_rotation.weekend_tech_count + weekend_difference
        elif not weekend_difference:
            weekend_tech_index = 0

        for _shift in self.tech_schedule:
            if _shift.day_of_week == 1:
                _shift.caregiver_id_num = self.weekend_rotation.tech_schedule[weekend_tech_index].caregiver_id_number
            if _shift.day_of_week == 7:
                if weekend_tech_index < self.weekend_rotation.weekend_rph_count:
                    weekend_tech_index += 1
                else:
                    weekend_tech_index = 0
                _shift.caregiver_id_num = self.weekend_rotation.tech_schedule[weekend_tech_index].caregiver_id_number

    def assign_cant_dates_rph(self):
        """ Assign cant_dates based on the schedule and on time-off requests """

        # if RPh caregiver works a weekend, they get the following Friday off.
        for _shift in self.rph_schedule:
            if _shift.day_of_week == 1:
                for _caregiver in self.team:
                    if _caregiver.caregiver_id_num == _shift.caregiver_id_num:
                        _caregiver.cant_dates.add(date(_shift.year, _shift.month, _shift.day_of_month) + timedelta(5))

        # accept time-off requests
        self.accept_time_off_requests("Pharmacist")

    def assign_cant_dates_tech(self):
        """ Assign cant_dates based on the schedule and on time-off requests """

        # accept time-off requests
        self.accept_time_off_requests("Technician")

    def accept_time_off_requests(self, caregiver_descriptor):
        """ Accept time-off requests based on caregiver type and assign cant_dates to the respective schedule """
        while True:
            caregiver_id = input(f"Please enter the {caregiver_descriptor} Caregiver ID# "
                                 f"who has a time-off request, or [ENTER] for none: ")
            if caregiver_id == "":
                break
            time_off_date = input("Please enter the date of the time-off request for this caregiver "
                                  "in the format of MM/DD/YYYY, or [ENTER] for none: ")
            if time_off_date == "":
                break
            time_off_date = date(int(time_off_date[6:10]), int(time_off_date[0:2]), int(time_off_date[3:5]))
            for _caregiver in self.team:
                if _caregiver.caregiver_id_num == caregiver_id:
                    _caregiver.cant_dates.add(time_off_date)

    def create_initial(self, schedule, shift_length, caregiver_type):
        """ Create assignable_team, a list of AssignableCaregiver objects, each having 2 attributes,
            the caregiver and the remaining hours yet to be assigned for them for that week.
            If the Caregiver works a number of hours per pay period that when divided in
            half is not divisible by the shift length, then determine from a reference date in this method,
            which week of the pay period is being assigned, then apportion the shifts for that caregiver so that the
            first week, the remaining hours are rounded up to the nearest shift size, and the second week, the remaining
            hours are rounded down to the nearest shift size.
            Per-diem caregivers are not added to the assignable caregiver list.
            Loop through the team and assign the correct number of remaining hours to each caregiver.
            Deduct the hours already assigned in that week of the Caregiver schedule from the remaining hours
            Randomly select a Pharmacist caregiver, then randomly select a shift, and if RPh has remaining hours,
            and if there is no mismatch of skills, then assign the Caregiver to the shift. """

        extra_shifts = []
        reference_date_start_of_pay_period = datetime(2023, 12, 3)
        start_day = datetime(schedule[0].year, schedule[0].month, schedule[0].day)
        week_difference = (start_day - reference_date_start_of_pay_period).days
        pay_period_week = 1
        if week_difference % 14 != 0:
            pay_period_week = 2
        for _week in range(1, schedule[-1].week_of_month + 1):
            assignable_team = []
            for _caregiver in self.team:
                # skip per-diem caregivers who have 0 minimum hours
                if _caregiver.min_hours == 0:
                    continue
                remaining_hours = _caregiver.min_hours / 2
                if remaining_hours % shift_length != 0:
                    if pay_period_week == 1:
                        remaining_hours += (shift_length / 2)
                    elif pay_period_week == 2:
                        remaining_hours -= (shift_length / 2)
                assignable_team.append(AssignableCaregiver(_caregiver, remaining_hours))

            # provide a count of shifts in this week
            shift_count = 0
            for _shift in schedule:
                if _shift.week_of_month == _week:
                    shift_count += 1

            # provide a count of remaining hours for the entire assignable team in this week
            total_remaining_hours = 0
            for assignee in assignable_team:
                total_remaining_hours += assignee.caregiver.remaining_hours

            # As long as there are remaining hours amongst the assignable team, randomly try to assign a caregiver
            # to their schedule.  If there are remaining caregivers after exhausting available shifts,
            # random shifts will be added to the list extra_shifts, which is added back to the schedule finally.
            while total_remaining_hours:
                assignee = choice(assignable_team)
                shift_assignment = choice(range(((_week - 1) * shift_count), ((_week * shift_count) + 1)))
                if (not schedule[shift_assignment].caregiver_id_num and (assignee.remaining_hours != 0)
                        and Assignment.skills_no_mismatch(assignee.caregiver, schedule[shift_assignment])
                        and (date(schedule[shift_assignment].year, schedule[shift_assignment].month,
                                  schedule[shift_assignment].day) not in assignee.caregiver.cant_dates)):
                    schedule[shift_assignment].caregiver_id_num = assignee.caregiver.caregiver_id_num
                    assignee.remaining_hours -= shift_length
                    shift_count -= 1
                    if assignee.remaining_hours == 0:
                        assignable_team.remove(assignee)
                    for assignee in assignable_team:
                        total_remaining_hours += assignee.caregiver.remaining_hours
                    if total_remaining_hours and not shift_count:
                        for _assignee in assignable_team:
                            random_day = choice([2, 3, 4, 5, 6])
                            random_day_start = choice([7, 7, 7.5, 7.5])
                            if random_day_start == 7:
                                random_location = Location.INPATIENT
                            else:
                                random_location = Location.RETAIL
                            extra_shifts.append(Shift(day_of_week=random_day, location=random_location,
                                                      start_time=random_day_start,
                                                      end_time=(random_day_start + shift_length + 0.5),
                                                      caregiver_type=caregiver_type, skills=set()))
            pay_period_week = 2 if pay_period_week == 1 else 1
        for extra_shift in extra_shifts:
            # Extra shifts are tacked on to the end, but unsure if they should be inserted within the schedule?
            schedule.append(extra_shift)
        return schedule

    def refinement(self):
        """ Method to refine the schedule based on Evaluation instance """
        
        # Calculate before score. 
        self.evaluation.evaluate()
        before_score = self.evaluation.shift_locations.score + self.evaluation.shift_times_score
        
        # Make a change to the schedule among non-perdiem Caregivers that doesn't violate any cant_dates or must_dates. 
        # ===== unfinished method!!
        for shift in self.rph_schedule:
            shift_min_choice = choice(self.evaluation.scores_rph_min_variety)
            shift_max_choice = choice(self.evaluation.scores_rph_max_variety)
            shift_min_choice, shift_max_choice = shift_max_choice, shift_min_choice
        
        # Calculate the after score. 
        self.evaluation.evaluate()
        after_score = self.evaluation.shift_locations.score + self.evaluation.shift_times_score
        
        # If the before score is greater or equal to the after score, undo the schedule change. 
        pass
