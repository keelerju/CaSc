from template import Template


class Schedule:
    """ A class to describe the entire schedule """

    def __init__(self, year, month, repeats=1):
        self.repeats = repeats
        self.year = year
        self.month = month
        self.template = Template()
