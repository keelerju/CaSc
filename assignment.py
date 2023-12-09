from datetime import date
from random import choice


class Assignment:
    """ Class with methods that accept schedules, team, and evaluation objects, which employs various strategy methods
    for initial assignment and refinement methods """

    def __init__(self):
        pass

    def initial_assignment(self, rph_schedule, tech_schedule, team, evaluation):
        for _caregiver in team.team:
            if _caregiver.must_dates:
                for _date in _caregiver.must_dates:
                    pass
        random_shift = random.choice(rph_schedule)

    def refinement(self, rph_schedule, tech_schedule, team, evaluation):
        pass
