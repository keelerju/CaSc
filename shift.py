from location import Location
from caregivertype import CaregiverType


class Shift:
    """ Class representation of a shift """
    def __init__(self, *,
                 day_of_week=0, year=2023, month=1, day_of_month=1, location=Location(5), start_time=0, end_time=0,
                 caregiver_type=(), special_reqs=(), caregiver_id_num=0):

        # Sunday is day 1
        self.day_of_week = day_of_week
        self.year = year
        self.month = month
        self.day_of_month = day_of_month
        self.location = Location(location)
        self.start_time = start_time
        self.end_time = end_time
        self.caregiver_type = (CaregiverType(caregiver_type))
        self.special_reqs = [special_reqs]
        self.caregiver_id_num = caregiver_id_num
