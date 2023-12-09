from shift import Shift
from caregivertype import CaregiverType
from location import Location


class Template:
    """ A class representing a week-long schedule template containing 
    no specific year/month/date information or caregiver assignments"""

    def __init__(self):
        """ Instantiates templates as lists that will hold shift objects,
        then builds available templates with all possible shifts """
        self.rph_template = []
        self.tech_template = []
        self.build_templates()

    def build_templates(self):
        self.build_rph_template()
        self.build_tech_template()

    def build_rph_template(self):
        # Sunday
        self.rph_template.append(Shift(
            day_of_week=1, location=Location.INPATIENT, start_time=7.5, end_time=16,
            caregiver_type=CaregiverType.RPH, special_reqs=set()))

        # Monday
        self.rph_template.append(Shift(
            day_of_week=2, location=Location.RETAIL, start_time=7.5, end_time=18,
            caregiver_type=CaregiverType.RPH, special_reqs=set()))
        self.rph_template.append(Shift(
            day_of_week=2, location=Location.RETAIL, start_time=7.5, end_time=18,
            caregiver_type=CaregiverType.RPH, special_reqs=set()))
        self.rph_template.append(Shift(
            day_of_week=2, location=Location.INPATIENT, start_time=7, end_time=17.5,
            caregiver_type=CaregiverType.RPH, special_reqs=set()))
        self.rph_template.append(Shift(
            day_of_week=2, location=Location.INPATIENT, start_time=7, end_time=17.5,
            caregiver_type=CaregiverType.RPH, special_reqs=set()))

        # Tuesday
        self.rph_template.append(Shift(
            day_of_week=3, location=Location.RETAIL, start_time=7.5, end_time=18,
            caregiver_type=CaregiverType.RPH, special_reqs=set()))
        self.rph_template.append(Shift(
            day_of_week=3, location=Location.RETAIL, start_time=7.5, end_time=18,
            caregiver_type=CaregiverType.RPH, special_reqs=set()))
        self.rph_template.append(Shift(
            day_of_week=3, location=Location.INPATIENT, start_time=7, end_time=17.5,
            caregiver_type=CaregiverType.RPH, special_reqs=set()))
        self.rph_template.append(Shift(
            day_of_week=3, location=Location.INPATIENT, start_time=7, end_time=17.5,
            caregiver_type=CaregiverType.RPH, special_reqs=set()))

        # Wednesday
        self.rph_template.append(Shift(
            day_of_week=4, location=Location.RETAIL, start_time=7.5, end_time=18,
            caregiver_type=CaregiverType.RPH, special_reqs=set()))
        self.rph_template.append(Shift(
            day_of_week=4, location=Location.RETAIL, start_time=7.5, end_time=18,
            caregiver_type=CaregiverType.RPH, special_reqs=set()))
        self.rph_template.append(Shift(
            day_of_week=4, location=Location.INPATIENT, start_time=7, end_time=17.5,
            caregiver_type=CaregiverType.RPH, special_reqs=set()))
        self.rph_template.append(Shift(
            day_of_week=4, location=Location.INPATIENT, start_time=7, end_time=17.5,
            caregiver_type=CaregiverType.RPH, special_reqs={"CHEMO"}))

        # Thursday
        self.rph_template.append(Shift(
            day_of_week=5, location=Location.RETAIL, start_time=7.5, end_time=18,
            caregiver_type=CaregiverType.RPH, special_reqs=set()))
        self.rph_template.append(Shift(
            day_of_week=5, location=Location.RETAIL, start_time=7.5, end_time=18,
            caregiver_type=CaregiverType.RPH, special_reqs=set()))
        self.rph_template.append(Shift(
            day_of_week=5, location=Location.INPATIENT, start_time=7, end_time=17.5,
            caregiver_type=CaregiverType.RPH, special_reqs=set()))
        self.rph_template.append(Shift(
            day_of_week=5, location=Location.INPATIENT, start_time=7, end_time=17.5,
            caregiver_type=CaregiverType.RPH, special_reqs={"CHEMO"}))

        # Friday
        self.rph_template.append(Shift(
            day_of_week=6, location=Location.RETAIL, start_time=7.5, end_time=18,
            caregiver_type=CaregiverType.RPH, special_reqs=set()))
        self.rph_template.append(Shift(
            day_of_week=6, location=Location.RETAIL, start_time=7.5, end_time=18,
            caregiver_type=CaregiverType.RPH, special_reqs=set()))
        self.rph_template.append(Shift(
            day_of_week=6, location=Location.INPATIENT, start_time=7, end_time=17.5,
            caregiver_type=CaregiverType.RPH, special_reqs=set()))
        self.rph_template.append(Shift(
            day_of_week=6, location=Location.INPATIENT, start_time=7, end_time=17.5,
            caregiver_type=CaregiverType.RPH, special_reqs=set()))

        # Saturday
        self.rph_template.append(Shift(
            day_of_week=7, location=Location.INPATIENT, start_time=7.5, end_time=16,
            caregiver_type=CaregiverType.RPH, special_reqs=set()))

    def build_tech_template(self):
        # Sunday
        self.tech_template.append(Shift(
            day_of_week=1, location=Location.INPATIENT, start_time=7.5, end_time=16,
            caregiver_type=CaregiverType.TECH, special_reqs=set()))

        # Monday
        self.tech_template.append(Shift(
            day_of_week=2, location=Location.RETAIL, start_time=7.5, end_time=16,
            caregiver_type=CaregiverType.TECH, special_reqs=set()))
        self.tech_template.append(Shift(
            day_of_week=2, location=Location.RETAIL, start_time=8.5, end_time=17,
            caregiver_type=CaregiverType.TECH, special_reqs=set()))
        self.tech_template.append(Shift(
            day_of_week=2, location=Location.RETAIL, start_time=9.5, end_time=18,
            caregiver_type=CaregiverType.TECH, special_reqs=set()))
        self.tech_template.append(Shift(
            day_of_week=2, location=Location.INPATIENT, start_time=7, end_time=15.5,
            caregiver_type=CaregiverType.TECH, special_reqs=set()))
        self.tech_template.append(Shift(
            day_of_week=2, location=Location.INPATIENT, start_time=9, end_time=17.5,
            caregiver_type=CaregiverType.TECH, special_reqs=set()))

        # Tuesday
        self.tech_template.append(Shift(
            day_of_week=3, location=Location.RETAIL, start_time=7.5, end_time=16,
            caregiver_type=CaregiverType.TECH, special_reqs=set()))
        self.tech_template.append(Shift(
            day_of_week=3, location=Location.RETAIL, start_time=8.5, end_time=17,
            caregiver_type=CaregiverType.TECH, special_reqs=set()))
        self.tech_template.append(Shift(
            day_of_week=3, location=Location.RETAIL, start_time=9.5, end_time=18,
            caregiver_type=CaregiverType.TECH, special_reqs=set()))
        self.tech_template.append(Shift(
            day_of_week=3, location=Location.INPATIENT, start_time=7, end_time=15.5,
            caregiver_type=CaregiverType.TECH, special_reqs=set()))
        self.tech_template.append(Shift(
            day_of_week=3, location=Location.INPATIENT, start_time=9, end_time=17.5,
            caregiver_type=CaregiverType.TECH, special_reqs=set()))

        # Wednesday
        self.tech_template.append(Shift(
            day_of_week=4, location=Location.RETAIL, start_time=7.5, end_time=16,
            caregiver_type=CaregiverType.TECH, special_reqs=set()))
        self.tech_template.append(Shift(
            day_of_week=4, location=Location.RETAIL, start_time=8.5, end_time=17,
            caregiver_type=CaregiverType.TECH, special_reqs=set()))
        self.tech_template.append(Shift(
            day_of_week=4, location=Location.RETAIL, start_time=9.5, end_time=18,
            caregiver_type=CaregiverType.TECH, special_reqs=set()))
        self.tech_template.append(Shift(
            day_of_week=4, location=Location.INPATIENT, start_time=7, end_time=15.5,
            caregiver_type=CaregiverType.TECH, special_reqs=set()))
        self.tech_template.append(Shift(
            day_of_week=4, location=Location.INPATIENT, start_time=9, end_time=17.5,
            caregiver_type=CaregiverType.TECH, special_reqs=set()))

        # Thursday
        self.tech_template.append(Shift(
            day_of_week=5, location=Location.RETAIL, start_time=7.5, end_time=16,
            caregiver_type=CaregiverType.TECH, special_reqs=set()))
        self.tech_template.append(Shift(
            day_of_week=5, location=Location.RETAIL, start_time=8.5, end_time=17,
            caregiver_type=CaregiverType.TECH, special_reqs=set()))
        self.tech_template.append(Shift(
            day_of_week=5, location=Location.RETAIL, start_time=9.5, end_time=18,
            caregiver_type=CaregiverType.TECH, special_reqs=set()))
        self.tech_template.append(Shift(
            day_of_week=5, location=Location.INPATIENT, start_time=7, end_time=15.5,
            caregiver_type=CaregiverType.TECH, special_reqs=set()))
        self.tech_template.append(Shift(
            day_of_week=5, location=Location.INPATIENT, start_time=9, end_time=17.5,
            caregiver_type=CaregiverType.TECH, special_reqs=set()))

        # Friday
        self.tech_template.append(Shift(
            day_of_week=6, location=Location.RETAIL, start_time=7.5, end_time=16,
            caregiver_type=CaregiverType.TECH, special_reqs=set()))
        self.tech_template.append(Shift(
            day_of_week=6, location=Location.RETAIL, start_time=8.5, end_time=17,
            caregiver_type=CaregiverType.TECH, special_reqs=set()))
        self.tech_template.append(Shift(
            day_of_week=6, location=Location.RETAIL, start_time=9.5, end_time=18,
            caregiver_type=CaregiverType.TECH, special_reqs=set()))
        self.tech_template.append(Shift(
            day_of_week=6, location=Location.INPATIENT, start_time=7, end_time=15.5,
            caregiver_type=CaregiverType.TECH, special_reqs=set()))
        self.tech_template.append(Shift(
            day_of_week=6, location=Location.INPATIENT, start_time=9, end_time=17.5,
            caregiver_type=CaregiverType.TECH, special_reqs=set()))

        # Saturday
        self.tech_template.append(Shift(
            day_of_week=7, location=Location.INPATIENT, start_time=7.5, end_time=16,
            caregiver_type=CaregiverType.TECH, special_reqs=set()))
