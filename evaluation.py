class Evaluation:
    """ Class that contains evaluation methods that will apply to the refinement methods of the assignment class """

    def __init__(self, rph_schedule, tech_schedule, team):
        self.rph_schedule = rph_schedule
        self.tech_schedule = tech_schedule
        self.team = team

    def evaluate(self):
        """ Evaluate each schedule for the various criteria and generate criteria scores and a composite score. """

        # Evaluate based on variety of shift locations per Caregiver
        for shift in self.rph_schedule:
            pass

        # Evaluate based on number of shifts in either Inpatient or Retail pharmacy per Caregiver
        for shift in self.rph_schedule:
            pass

        # Evaluate based on variety of start times per Caregiver
        for shift in self.rph_schedule:
            pass
