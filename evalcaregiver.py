from caregivertype import CaregiverType

class EvalCaregiver:
    """ Class to provide attributes that can be tallied to generate scores for schedule evaluations """
    def __init__(self, caregiver_id_num, caregiver_type):
        self.caregiver_id_num = caregiver_id_num
        self.caregiver_type = caregiver_type
        self.inpatient_locs = 0
        self.retail_locs = 0
        self.time0700_rph = 0
        self.time0730wd_rph = 0
        self.time0700_tech = 0
        self.time0900_tech = 0
        self.time0730wd_tech = 0
        self.time0830_tech = 0
        self.time0930_tech = 0