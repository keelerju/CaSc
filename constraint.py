class Constraint:
    """ Class representation of a constraint """

    def __init__(self, *, date, criteria, employee_id_num):
        self.date = date
        self.criteria = criteria
        self.employee_id_num = employee_id_num
