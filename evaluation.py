from evalcaregiver import EvalCaregiver
from location import Location
import statistics


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
        self.shift_locations_rph_score = 0
        self.shift_locations_tech_score = 0
        
        self.shift_times_score = 0
        self.shift_times_rph_score = 0
        self.shift_times_tech_score = 0

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
                        break
        
        for _shift in rph_schedule:
            if _shift.location == Location.RETAIL:
                for _eval_cg in self.eval_team:
                    if _shift.caregiver_id_num == _eval_cg.caregiver_id_num:
                        _eval_cg.retail_locs += 1
                        break
        
        for _shift in tec_schedule:
            if _shift.location == Location.INPATIENT:
                for _eval_cg in self.eval_team:
                    if _shift.caregiver_id_num == _eval_cg.caregiver_id_num:
                        _eval_cg.inpatient_locs += 1
                        break
        
        for _shift in tech_schedule:
            if _shift.location == Location.RETAIL:
                for _eval_cg in self.eval_team:
                    if _shift.caregiver_id_num == _eval_cg.caregiver_id_num:
                        _eval_cg.retail_locs += 1
                        break
        
        eval_team_rph_inpt_locs = []
        eval_team_rph_retail_locs = []
        
        for _eval_cg in eval_team:
            eval_team_rph_inpt_locs.append(_eval_cg.inpt_locs)
            eval_team_rph_retail_locs.append(_eval_cg.retail_locs)
        
        inpt_rph_variance = variance(eval_team_rph_inpt_locs)
        retail_rph_variance = variance(eval_team_rph_retail_locs)
        
        self.shift_locations_rph_score = ( (inpt_variance + retail_variance) * len(team.team))
        
        self.shift_locations_score = self.shift_locations_rph_score + self.shift_locations_tech_score
    
    def evaluate_shift_times(self):
        """ Evaluate based on variety of shift times per Caregiver """
        
        eval_team_rph_0700s = []
        eval_team_rph_0730wds = []
        
        eval_team_tech_0700s = []
        eval_team_tech_0900s = []
        eval_team_tech_0730s = []
        eval_team_tech_0830s = []
        eval_team_tech_0930s = []
        
        for _shift in rph_schedule:
            if _shift_start_time == 7:
                for _eval_cg in self.eval_team:
                    if _shift.caregiver_id_num == _eval_cg.caregiver_id_num:
                        _eval_cg.time0700 += 1
        
        for _shift in tech_schedule:
            pass
        
        
    