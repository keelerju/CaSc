class Constraint:
    """ Class representation of a constraint """

    def __init__(self, *, date, criteria, value):
        self.date = date
        self.criteria = criteria
        self.value = value
