from evalcaregiver import EvalCaregiver
from location import Location


class Evaluation:
    """ Class that contains evaluation methods that will apply to the refinement methods of the assignment class """

    def __init__(self, rph_schedule, tech_schedule, team):
        self.rph_schedule = rph_schedule
        self.tech_schedule = tech_schedule
        self.team = team
        self.eval_team = []
        
        for _caregiver in self.team:
            self.eval_team.append(EvalCaregiver(_caregiver.caregiver_id_num))
        
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
            if _shift.location == Location.INPATIENT:
                for _eval_cg in self.eval_team:
                    if _shift.caregiver_id_num == _eval_cg.caregiver_id_num:
                        _eval_cg.inpatient_locs += 1
        
        for _shift in rph_schedule:
            if _shift.location == Location.RETAIL:
                for _eval_cg in self.eval_team:
                    if _shift.caregiver_id_num == _eval_cg.caregiver_id_num:
                        _eval_cg.retail_locs += 1
        
        for _shift in tech_schedule:
            pass
    
    def evaluate_shift_times(self):
        """ Evaluate based on variety of shift times per Caregiver """
        
        for _shift in rph_schedule:
            if _shift_start_time == 7:
                for _eval_cg in self.eval_team:
                    if _shift.caregiver_id_num == _eval_cg.caregiver_id_num:
                        _eval_cg.time0700 += 1
        
        for _shift in tech_schedule:
            pass
    