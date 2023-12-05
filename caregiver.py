from caregivertype import CaregiverType


class Caregiver:
    """A class to represent a caregiver """

    def __init__(self, *, name='Caregiver', caregiver_id_num=0, caregiver_type=CaregiverType(5),
                 min_hours=80, attributes=None, must_dates=None, cant_dates=None):
        self.name = name
        self.caregiver_id_num = caregiver_id_num
        self.caregiver_type = CaregiverType(caregiver_type)
        self.min_hours = min_hours
        if not attributes:
            self.attributes = set()
        else:
            self.attributes = set(attributes)
        if not must_dates:
            must_dates = set()
        else:
            self.must_dates = set(must_dates)
        if not cant_dates:
            self.cant_dates = set()
        else:
            self.cant_date = set(cant_dates)
