from caregivertype import CaregiverType


class Caregiver:
    """A class to represent a caregiver """

    def __init__(self, *, name='Caregiver', caregiver_id_num=0, caregiver_type=CaregiverType(5),
                 min_hours=80, is_chemo_mixer=False, no_dates=(), must_dates=()):
        self.name = name
        self.caregiver_id_num = caregiver_id_num
        self.caregiver_type = CaregiverType(caregiver_type)
        self.min_hours = min_hours
        self.is_chemo_mixer = is_chemo_mixer
        self.no_dates = no_dates
        self.must_dates = must_dates
