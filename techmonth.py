from shift import Shift
from caregivertype import CaregiverType
from location import Location
import calendar
import copy


class TechMonth:
    """ A class representing the month schedule for Pharmacists """

    def __init__(self, year, month):
        self.tech_schedule = []
        self.year = year
        self.month = month

    # static method to convert out of the format of the calendar module
    # to format where weekdays are 1-indexed, and Sunday is Day 1
    @staticmethod
    def convert(wd):
        return 1 if wd == 6 else wd + 2

    def fill_blank(self, tech_template, holidays):

        # create 3 templates that will include year/month information for
        # the month previous, the month of, and the month after
        tech_template_prev = copy.deepcopy(tech_template)
        tech_template_current = copy.deepcopy(tech_template)
        tech_template_after = copy.deepcopy(tech_template)

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
        for s in tech_template_prev:
            s.year = year_of_prev_month
            s.month = month_prev
        # Current month
        for s in tech_template_current:
            s.year = self.year
            s.month = self.month
        # Month after
        if self.month == 12:
            month_after = 1
            year_of_month_after = self.year + 1
        else:
            month_after = self.month + 1
        for s in tech_template_after:
            s.year = year_of_month_after
            s.month = month_after

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

        # loop through shifts of the last week of the previous month and append shifts to tech_schedule
        weekday = 1
        day_of_month = 1
        ignore_days = False
        if weekday_of_first_day_of_current_month != 1:
            day_of_month = last_sunday_day_of_month_prev
            ignore_days = True
            for s in tech_template_prev:
                if s.day_of_week > weekday:
                    day_of_month = day_of_month + 1
                    weekday = s.day_of_week
                    if weekday > weekday_of_last_day_of_month_prev:
                        break
                s.day_of_month = day_of_month
                self.tech_schedule.append(s)

        # loop through shifts of the first week of the current month and append shifts to tech_schedule
        day_of_month = 1
        for s in copy.deepcopy(tech_template_current):
            if ignore_days and (s.day_of_week < weekday):
                continue
            ignore_days = False
            if s.day_of_week > weekday:
                day_of_month = day_of_month + 1
                weekday = s.day_of_week
            s.day_of_month = day_of_month
            self.tech_schedule.append(s)

        # loop through shifts of subsequent weeks of the current month and append shifts to tech_schedule
        weekday = 1
        day_of_month = day_of_month + 1
        for w in range(int((num_of_days_in_current_month - day_of_month) / 7 + 1)):
            for s in copy.deepcopy(tech_template_current):
                if s.day_of_week != weekday:
                    day_of_month = day_of_month + 1
                    weekday = s.day_of_week
                if day_of_month > num_of_days_in_current_month:
                    break
                s.day_of_month = day_of_month
                self.tech_schedule.append(s)

        # loop through shifts of the first partial week of the next month and append shifts to tech_schedule
        if weekday_of_last_day_of_current_month != 7:
            day_of_month = 1
            for s in tech_template_after:
                if s.day_of_week < weekday:
                    continue
                if s.day_of_week > weekday:
                    day_of_month = day_of_month + 1
                    weekday = s.day_of_week
                s.day_of_month = day_of_month
                self.tech_schedule.append(s)
            if holidays:
                self.add_holidays(holidays)

    def add_holidays(self, holidays):
        r = []
        first_instance = True
        for s in self.tech_schedule:
            for holiday in holidays:
                if (s.day_of_month == holiday.day) and s.month == holiday.month and first_instance:
                    weekday_of_holiday = self.convert(calendar.weekday(holiday.year, holiday.month, holiday.day))
                    r.append(Shift(
                        day_of_week=weekday_of_holiday, day_of_month=holiday.day, location=Location.INPATIENT,
                        start_time=7.5, end_time=12, caregiver_type=CaregiverType.TECH, special_reqs=()))
                    first_instance = False
                elif (s.day_of_month == holiday.day) and (s.month == holiday.month) and not first_instance:
                    pass
                elif s.day_of_week != holiday:
                    r.append(s)
        self.tech_schedule = r

    def print_schedule(self):
        print()
        for s in self.tech_schedule:
            print(vars(s))

    def fill_must(self):
        pass

    def random_assign(self):
        pass
