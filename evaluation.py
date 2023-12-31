from evalcaregiver import EvalCaregiver
from caregivertype import CaregiverType
from location import Location
from statistics import variance


class Evaluation:
    """ Class that contains evaluation methods that will apply to the refinement methods of the assignment class """

    def __init__(self, rph_schedule, tech_schedule, team):
        self.rph_schedule = rph_schedule
        self.tech_schedule = tech_schedule
        self.team = team
        self.eval_team = []
        
        # Fill the eval_team list with caregivers for purpose of tallying and evaluation.
        for _caregiver in self.team:
            self.eval_team.append(EvalCaregiver(_caregiver.caregiver_id_num, _caregiver.caregiver_type))
        
        # Score attributes that will be used to evaluate if incremental changes
        # to the schedule are improvements.
        self.shift_locations_score = 0
        self.shift_locations_rph_score = 0
        self.shift_locations_tech_score = 0
        
        self.shift_times_score = 0
        self.shift_times_rph_score = 0
        self.shift_times_tech_score = 0

        self.shift_locations_min_variety_rph_id = 0
        self.shift_locations_max_variety_rph_id = 0

        self.shift_locations_min_variety_tech_id = 0
        self.shift_locations_max_variety_tech_id = 0

    def evaluate(self):
        # Evaluate each schedule for the various criteria and generate criteria scores and a composite score.
        # This method can be called before/after a schedule change to compare scores. 
        # This method will call all other methods that generate scores from the schedule.
        # Each method called will update the score attributes.
        self._evaluate_shift_locations()
        self._evaluate_shift_times()
    
    def _evaluate_shift_locations(self):
        # Evaluate schedule based on variety of shift locations per Caregiver. 

        # Firstly, update the tallies for each eval_team caregiver for
        # the number of inpatient and retail shifts they each work.
        
        for _shift in self.rph_schedule:
            if _shift.location == Location.INPATIENT:
                for _eval_cg in self.eval_team:
                    if _shift.caregiver_id_num == _eval_cg.caregiver_id_num:
                        _eval_cg.inpatient_locs += 1
                        break
        
        for _shift in self.rph_schedule:
            if _shift.location == Location.RETAIL:
                for _eval_cg in self.eval_team:
                    if _shift.caregiver_id_num == _eval_cg.caregiver_id_num:
                        _eval_cg.retail_locs += 1
                        break
        
        for _shift in self.tech_schedule:
            if _shift.location == Location.INPATIENT:
                for _eval_cg in self.eval_team:
                    if _shift.caregiver_id_num == _eval_cg.caregiver_id_num:
                        _eval_cg.inpatient_locs += 1
                        break
        
        for _shift in self.tech_schedule:
            if _shift.location == Location.RETAIL:
                for _eval_cg in self.eval_team:
                    if _shift.caregiver_id_num == _eval_cg.caregiver_id_num:
                        _eval_cg.retail_locs += 1
                        break
        
        # Secondly, lists are created, where each element is
        # the number of respective shift locations for each caregiver.
        
        eval_team_rph_inpt_locs = []
        eval_team_rph_retail_locs = []
        
        eval_team_tech_inpt_locs = []
        eval_team_tech_retail_locs = []
        
        min_variety_rph = 0
        max_variety_rph = 0
        min_variety_tech = 0
        max_variety_tech = 0
        
        for _eval_cg in self.eval_team:
            if _eval_cg.caregiver_type == CaregiverType.RPH:
                eval_team_rph_inpt_locs.append(_eval_cg.inpatient_locs)
                eval_team_rph_retail_locs.append(_eval_cg.retail_locs)
                if min_variety_rph == 0 or max_variety_rph == 0:
                    self.shift_locations_min_variety_rph_id = _eval_cg.caregiver_id_num
                    self.shift_locations_max_variety_rph_id = _eval_cg.caregiver_id_num
                if min_variety_rph > _eval_cg.retail_locs:
                    self.shift_locations_min_variety_rph_id = _eval_cg.caregiver_id_num
                if max_variety_rph < _eval_cg.retail_locs:
                    self.shift_locations_max_variety_rph_id = _eval_cg.caregiver_id_num
                
            if _eval_cg.caregiver_type == CaregiverType.TECH:
                eval_team_tech_inpt_locs.append(_eval_cg.inpatient_locs)
                eval_team_tech_retail_locs.append(_eval_cg.retail_locs)
                if min_variety_tech == 0 or max_variety_tech == 0:
                    self.shift_locations_min_variety_tech_id = _eval_cg.caregiver_id_num
                    self.shift_locations_max_variety_tech_id = _eval_cg.caregiver_id_num
                if min_variety_tech > _eval_cg.retail_locs:
                    self.shift_locations_min_variety_tech_id = _eval_cg.caregiver_id_num
                if max_variety_tech < _eval_cg.retail_locs:
                    self.shift_locations_max_variety_tech_id = _eval_cg.caregiver_id_num
        
        # Thirdly, variances are calculated based on the individual shift tallies.
        # The variances are divided by the number of caregivers to generate an attribute score.
        
        inpt_rph_loc_variance = variance(eval_team_rph_inpt_locs)
        retail_rph_loc_variance = variance(eval_team_rph_retail_locs)
        self.shift_locations_rph_score = \
            ((inpt_rph_loc_variance + retail_rph_loc_variance) /
             len([cg for cg in self.team if cg.caregiver_type == CaregiverType.RPH]))
        
        inpt_tech_variance = variance(eval_team_tech_inpt_locs)
        retail_tech_variance = variance(eval_team_tech_retail_locs)
        self.shift_locations_tech_score = \
            ((inpt_tech_variance + retail_tech_variance) /
             len([cg for cg in self.team if cg.caregiver_type == CaregiverType.TECH]))
        
        self.shift_locations_score = self.shift_locations_rph_score + self.shift_locations_tech_score

    def _evaluate_shift_times(self):
        # Evaluate schedule based on variety of shift times per Caregiver. 
        
        # Firstly, update the tallies for each eval_team caregiver for the number of
        # weekday shifts with specific start times they each work.
        
        for _shift in self.rph_schedule:
            if _shift.start_time == 7:
                for _eval_cg in self.eval_team:
                    if _shift.caregiver_id_num == _eval_cg.caregiver_id_num:
                        _eval_cg.time0700_rph += 1
                        break
        
        for _shift in self.rph_schedule:
            if _shift.start_time == 7.5 and _shift.day_of_week in range(2, 7):
                for _eval_cg in self.eval_team:
                    if _shift.caregiver_id_num == _eval_cg.caregiver_id_num:
                        _eval_cg.time0730wd_rph += 1
                        break
        
        for _shift in self.tech_schedule:
            if _shift.start_time == 7:
                for _eval_cg in self.eval_team:
                    if _shift.caregiver_id_num == _eval_cg.caregiver_id_num:
                        _eval_cg.time0700_tech += 1
                        break
        
        for _shift in self.tech_schedule:
            if _shift.start_time == 9:
                for _eval_cg in self.eval_team:
                    if _shift.caregiver_id_num == _eval_cg.caregiver_id_num:
                        _eval_cg.time0900_tech += 1
                        break
        
        for _shift in self.tech_schedule:
            if _shift.start_time == 7.5 and _shift.day_of_week in range(2, 7):
                for _eval_cg in self.eval_team:
                    if _shift.caregiver_id_num == _eval_cg.caregiver_id_num:
                        _eval_cg.time0730wd_tech += 1
                        break
        
        for _shift in self.tech_schedule:
            if _shift.start_time == 8.5:
                for _eval_cg in self.eval_team:
                    if _shift.caregiver_id_num == _eval_cg.caregiver_id_num:
                        _eval_cg.time0830_tech += 1
                        break
                        
        for _shift in self.tech_schedule:
            if _shift.start_time == 9.5:
                for _eval_cg in self.eval_team:
                    if _shift.caregiver_id_num == _eval_cg.caregiver_id_num:
                        _eval_cg.time0930_tech += 1
                        break
        
        # Secondly, lists are created, where each element is the number of
        # respective weekday shift start times for each caregiver.
        
        eval_team_rph_0700 = []
        eval_team_rph_0730wd = []
        eval_team_tech_0700 = []
        eval_team_tech_0900 = []
        eval_team_tech_0730wd = []
        eval_team_tech_0830 = []
        eval_team_tech_0930 = []
        
        for _eval_cg in self.eval_team:
            if _eval_cg.caregiver_type == CaregiverType.RPH:
                eval_team_rph_0700.append(_eval_cg.time0700_rph)
                eval_team_rph_0730wd.append(_eval_cg.time0730wd_rph)
                
            if _eval_cg.caregiver_type == CaregiverType.TECH:
                eval_team_tech_0700.append(_eval_cg.time0700_tech)
                eval_team_tech_0900.append(_eval_cg.time0900_tech)
                eval_team_tech_0730wd.append(_eval_cg.time0730wd_tech)
                eval_team_tech_0830.append(_eval_cg.time0830_tech)
                eval_team_tech_0930.append(_eval_cg.time0930_tech)
        
        # Thirdly, variances are calculated based on the individual shift tallies.
        # The variances are divided by the number of caregivers to generate an attribute score.
        
        rph_0700_variance = variance(eval_team_rph_0700)
        rph_0730wd_variance = variance(eval_team_rph_0730wd)
        self.shift_times_rph_score = \
            ((rph_0700_variance + rph_0730wd_variance) /
             len([cg for cg in self.team if cg.caregiver_type == CaregiverType.RPH]))
        
        tech_0700_variance = variance(eval_team_tech_0700)
        tech_0900_variance = variance(eval_team_tech_0900)
        tech_0730wd_variance = variance(eval_team_rph_0730wd)
        tech_0830_variance = variance(eval_team_tech_0830)
        tech_0930_variance = variance(eval_team_tech_0930)
        self.shift_times_tech_score = \
            ((tech_0700_variance + tech_0900_variance + tech_0730wd_variance + tech_0830_variance + tech_0930_variance)
             / len([cg for cg in self.team if cg.caregiver_type == CaregiverType.TECH]))
        
        self.shift_times_score = self.shift_times_rph_score + self.shift_times_tech_score
        
    