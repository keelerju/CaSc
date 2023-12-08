from shift import Shift
from caregivertype import CaregiverType
from location import Location
import calendar
import copy


class RphMonth:
    """ A class representing the month schedule for Pharmacists """

    def __init__(self, year, month):
        self.rph_schedule = []
        self.year = year
        self.month = month

    # static method to convert out of the format of the calendar module
    # to format where weekdays are 1-indexed, and Sunday is Day 1
    @staticmethod
    def convert(wd):
        return 1 if wd == 6 else wd + 2

    def fill_blank(self, rph_template, holidays):

        # create 3 templates that will include year/month information for
        # the month previous, the month of, and the month after
        rph_template_prev = copy.deepcopy(rph_template)
        rph_template_current = copy.deepcopy(rph_template)
        rph_template_after = copy.deepcopy(rph_template)

        # establish local variables for use throughout scope
        year_of_prev_month, month_prev = self.year, self.month
        year_of_month_after, month_after = self.year, self.month

        # edit local variables to match actual years/months, and update the 3 templates
        # Previous month
        if self.month == 1:
            month_prev = 12
            year_of_prev_month = self.year - 1
        else:
            month_prev = self.month - 1
        for _shift in rph_template_prev:
            _shift.year = year_of_prev_month
            _shift.month = month_prev
        # Current month
        for _shift in rph_template_current:
            _shift.year = self.year
            _shift.month = self.month
        # Month after
        if self.month == 12:
            month_after = 1
            year_of_month_after = self.year + 1
        else:
            month_after = self.month + 1
        for _shift in rph_template_after:
            _shift.year = year_of_month_after
            _shift.month = month_after

        # determine the weekday of the 1st day of the month and the number of days of the month prior
        weekday_of_first_day_of_month_prev, num_of_days_in_month_prev = (
            calendar.monthrange(year_of_prev_month, month_prev))
        weekday_of_first_day_of_month_prev = self.convert(weekday_of_first_day_of_month_prev)

        # determine the weekday of the 1st day of the month and the number of days of the current month
        weekday_of_first_day_of_current_month, num_of_days_in_current_month = (
            calendar.monthrange(self.year, self.month))
        weekday_of_first_day_of_current_month = self.convert(weekday_of_first_day_of_current_month)

        # determine the weekday of the 1st day of the month and the number of days of the month after
        weekday_of_first_day_of_month_after, num_of_days_in_month_after = (
            calendar.monthrange(year_of_month_after, month_after))
        weekday_of_first_day_of_month_after = self.convert(weekday_of_first_day_of_month_after)

        # determine the weekday of the last day of the month previous
        weekday_of_last_day_of_month_prev = calendar.weekday(year_of_prev_month, month_prev, num_of_days_in_month_prev)
        weekday_of_last_day_of_month_prev = self.convert(weekday_of_last_day_of_month_prev)

        # determine the weekday of the last day of the current month
        weekday_of_last_day_of_current_month = calendar.weekday(self.year, self.month, num_of_days_in_current_month)
        weekday_of_last_day_of_current_month = self.convert(weekday_of_last_day_of_current_month)

        # determine the day of the previous month that the last Sunday falls
        last_sunday_day_of_month_prev = ((num_of_days_in_month_prev - weekday_of_last_day_of_month_prev) + 1)

        # loop through shifts of the last week of the previous month and append shifts to rph_schedule
        weekday = 1
        day_of_month = 1
        ignore_days = False
        if weekday_of_first_day_of_current_month != 1:
            day_of_month = last_sunday_day_of_month_prev
            ignore_days = True
            for _shift in rph_template_prev:
                if _shift.day_of_week > weekday:
                    day_of_month = day_of_month + 1
                    weekday = _shift.day_of_week
                    if weekday > weekday_of_last_day_of_month_prev:
                        break
                _shift.day_of_month = day_of_month
                self.rph_schedule.append(_shift)

        # loop through shifts of the first week of the current month and append shifts to rph_schedule
        day_of_month = 1
        for _shift in copy.deepcopy(rph_template_current):
            if ignore_days and (_shift.day_of_week < weekday):
                continue
            ignore_days = False
            if _shift.day_of_week > weekday:
                day_of_month = day_of_month + 1
                weekday = _shift.day_of_week
            _shift.day_of_month = day_of_month
            self.rph_schedule.append(_shift)

        # loop through shifts of subsequent weeks of the current month and append shifts to rph_schedule
        weekday = 1
        day_of_month = day_of_month + 1
        for _week in range(int((num_of_days_in_current_month - day_of_month) / 7 + 1)):
            for _shift in copy.deepcopy(rph_template_current):
                if _shift.day_of_week != weekday:
                    day_of_month = day_of_month + 1
                    weekday = _shift.day_of_week
                if day_of_month > num_of_days_in_current_month:
                    break
                _shift.day_of_month = day_of_month
                self.rph_schedule.append(_shift)

        # loop through shifts of the first partial week of the next month and append shifts to rph_schedule
        if weekday_of_last_day_of_current_month != 7:
            day_of_month = 1
            for _shift in rph_template_after:
                if _shift.day_of_week < weekday:
                    continue
                if _shift.day_of_week > weekday:
                    day_of_month = day_of_month + 1
                    weekday = _shift.day_of_week
                _shift.day_of_month = day_of_month
                self.rph_schedule.append(_shift)
            if holidays:
                self.add_holidays(holidays)

    def add_holidays(self, holidays):
        _rph_schedule_local = []
        first_instance = True
        for _shift in self.rph_schedule:
            for holiday in holidays:
                if (_shift.day_of_month == holiday.day) and _shift.month == holiday.month and first_instance:
                    weekday_of_holiday = self.convert(calendar.weekday(holiday.year, holiday.month, holiday.day))
                    _rph_schedule_local.append(Shift(
                        day_of_week=weekday_of_holiday, day_of_month=holiday.day, location=Location.INPATIENT,
                        start_time=7.5, end_time=12, caregiver_type=CaregiverType.RPH, special_reqs=()))
                    first_instance = False
                elif (_shift.day_of_month == holiday.day) and (_shift.month == holiday.month) and not first_instance:
                    pass
                elif _shift.day_of_week != holiday:
                    _rph_schedule_local.append(_shift)
        self.rph_schedule = _rph_schedule_local

    def print_schedule(self):
        print()
        for _shift in self.rph_schedule:
            print(vars(_shift))

    def fill_old(self, team):
        # create a list of lists of the shifts of the days from the month previous
        old_week = [[] for _ in range(6)]
        for _shift in rph_schedule:
            if _shift.month < self.month:
                old_week[_shift.day - 1].append(_shift)
            else:
                return
        
        # loop through the list, display shifts one day at a time, and assign caregivers
        for _day_of_week in old_week:
            if not _day_of_week:
                break
            for index, _shift in enumerate(index, _day_of_week):
                print(f"{index}.  {vars(_shift)}")
            for index, _shift in enumerate(index, _day_of_week):
                valid == True
                while valid:
                    number = input(f"Enter the Caregiver ID number assigned to shift {index}: ")
                    for _caregiver in team:
                        if number == _caregiver.caregiver_id_num:
                            _shift.caregivee_id_num = number
                            break
                        else:
                            valid ==False
                    if valid == True:
                        break
                    else:
                        print("Unknown caregiver.  Try again.")

        # add the caregivers back to the rph_schedule
        for index, _day_of_week in enumerate(old_week):
            if not _day_of_week:
                break
            for _shift in _day of week:
                self.rph_schedule[index] = _shift
