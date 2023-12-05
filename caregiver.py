from caregivertype import CaregiverType


class Caregiver:
    """A class to represent a caregiver """

    def __init__(self, *, name='Caregiver', caregiver_id_num=0, caregiver_type=CaregiverType(5),
                 min_hours=80, attributes=None, must_date=None, no_date=None):
        self.name = name
        self.caregiver_id_num = caregiver_id_num
        self.caregiver_type = CaregiverType(caregiver_type)
        self.min_hours = min_hours
        self.attributes = attributes
        self.must_date = must_date
        self.no_date = no_date
