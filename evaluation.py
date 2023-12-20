class Evaluation:
    """ Class that contains evaluation methods that will apply to the refinement methods of the assignment class """

    def __init__(self, rph_schedule, tech_schedule, team):
        self.rph_schedule = rph_schedule
        self.tech_schedule = tech_schedule
        self.team = team
        self.evaluated_team = []
        
        self.shift_locations_score = 0
        self.max_shift_locations_score = 0
        self.min_shift_locations_score = 0
        
        self.shift_locations_rph_score = 0
        self.max_shift_locations_rph_score = 0
        self.min_shift_locations_rph_score = 0
        
        self.shift_locations_tech_score = 0
        self.max_shift_locations_tech_score = 0
        self.min_shift_locations_tech_score = 0
        
        self.shift_times_score = 0
        self.max_shift_times_score = 0
        self.min_times_score = 0
        
        self.shift_times_rph_score = 0
        self.max_shift_times_rph_score = 0
        self.min_shift_times_rph_score = 0
        
        self.shift_times_tech_score = 0
        self.max_shift_times_tech_score = 0
        self.min_shift_times_tech_score = 0

    def evaluate(self):
        """ Evaluate each schedule for the various criteria and generate criteria scores and a composite score. """

        evaluate_shift_locations(self)
        evaluate_shift_times(self)
    
    def evaluate_shift_locations(self):
        """ Evaluate based on variety of shift locations per Caregiver """
        
        for _shift in rph_schedule:
            pass
        
        for _shift in tech_schedule:
            pass
    
    def evaluate_shift_times(self):
        """ Evaluate based on variety of shift times per Caregiver """
        
        for _shift in rph_schedule:
            pass
        
        for _shift in tech_schedule:
            pass
    