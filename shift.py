from location import Location
from caregivertype import CaregiverType


class Shift:
    """ Class representation of a shift """
    def __init__(self, *,
                 day_of_week=0, year=2023, month=1, day_of_month=1, week_of_month=1, location=Location(5), start_time=0, end_time=0,
                 caregiver_type=None, skills=None, caregiver_id_num=None, extra=False):

        # Sunday is day 1
        self.day_of_week = day_of_week
        self.year = year
        self.month = month
        self.day_of_month = day_of_month
        self.week_of_month = week_of_month
        self.location = Location(location)
        self.start_time = start_time
        self.end_time = end_time
        self.caregiver_type = (CaregiverType(caregiver_type))
        if not skills:
            self.skills = set()
        else:
            self.skills = set(skills)
        self.caregiver_id_num = caregiver_id_num
        
        # If extra is True, it represents that this is an extra shift to either accomodate 
        # overabundant caregivers or to provide needed coverage for high volume of work. 
        self.extra = extra
