class Constraint:
    """ Class representation of a constraint """

    def __init__(self, *, date, criteria, caregiver_id_num):
        self.date = date
        self.criteria = criteria
        self.caregiver_id_num = caregiver_id_num
