from shift import Shift
from caregivertype import CaregiverType
from location import Location
from skilltype import SkillType


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
            caregiver_type=CaregiverType.RPH, skills=set()))

        # Monday
        self.rph_template.append(Shift(
            day_of_week=2, location=Location.RETAIL, start_time=7.5, end_time=18,
            caregiver_type=CaregiverType.RPH, skills=set()))
        self.rph_template.append(Shift(
            day_of_week=2, location=Location.RETAIL, start_time=7.5, end_time=18,
            caregiver_type=CaregiverType.RPH, skills=set()))
        self.rph_template.append(Shift(
            day_of_week=2, location=Location.INPATIENT, start_time=7, end_time=17.5,
            caregiver_type=CaregiverType.RPH, skills=set()))
        self.rph_template.append(Shift(
            day_of_week=2, location=Location.INPATIENT, start_time=7, end_time=17.5,
            caregiver_type=CaregiverType.RPH, skills=set()))

        # Tuesday
        self.rph_template.append(Shift(
            day_of_week=3, location=Location.RETAIL, start_time=7.5, end_time=18,
            caregiver_type=CaregiverType.RPH, skills=set()))
        self.rph_template.append(Shift(
            day_of_week=3, location=Location.RETAIL, start_time=7.5, end_time=18,
            caregiver_type=CaregiverType.RPH, skills=set()))
        self.rph_template.append(Shift(
            day_of_week=3, location=Location.INPATIENT, start_time=7, end_time=17.5,
            caregiver_type=CaregiverType.RPH, skills=set()))
        self.rph_template.append(Shift(
            day_of_week=3, location=Location.INPATIENT, start_time=7, end_time=17.5,
            caregiver_type=CaregiverType.RPH, skills=set()))

        # Wednesday
        self.rph_template.append(Shift(
            day_of_week=4, location=Location.RETAIL, start_time=7.5, end_time=18,
            caregiver_type=CaregiverType.RPH, skills=set()))
        self.rph_template.append(Shift(
            day_of_week=4, location=Location.RETAIL, start_time=7.5, end_time=18,
            caregiver_type=CaregiverType.RPH, skills=set()))
        self.rph_template.append(Shift(
            day_of_week=4, location=Location.INPATIENT, start_time=7, end_time=17.5,
            caregiver_type=CaregiverType.RPH, skills=set()))
        self.rph_template.append(Shift(
            day_of_week=4, location=Location.INPATIENT, start_time=7, end_time=17.5,
            caregiver_type=CaregiverType.RPH, skills=set(SkillType.CHEMO)))

        # Thursday
        self.rph_template.append(Shift(
            day_of_week=5, location=Location.RETAIL, start_time=7.5, end_time=18,
            caregiver_type=CaregiverType.RPH, skills=set()))
        self.rph_template.append(Shift(
            day_of_week=5, location=Location.RETAIL, start_time=7.5, end_time=18,
            caregiver_type=CaregiverType.RPH, skills=set()))
        self.rph_template.append(Shift(
            day_of_week=5, location=Location.INPATIENT, start_time=7, end_time=17.5,
            caregiver_type=CaregiverType.RPH, skills=set()))
        self.rph_template.append(Shift(
            day_of_week=5, location=Location.INPATIENT, start_time=7, end_time=17.5,
            caregiver_type=CaregiverType.RPH, skills=set(SkillType.CHEMO)))

        # Friday
        self.rph_template.append(Shift(
            day_of_week=6, location=Location.RETAIL, start_time=7.5, end_time=18,
            caregiver_type=CaregiverType.RPH, skills=set()))
        self.rph_template.append(Shift(
            day_of_week=6, location=Location.RETAIL, start_time=7.5, end_time=18,
            caregiver_type=CaregiverType.RPH, skills=set()))
        self.rph_template.append(Shift(
            day_of_week=6, location=Location.INPATIENT, start_time=7, end_time=17.5,
            caregiver_type=CaregiverType.RPH, skills=set()))
        self.rph_template.append(Shift(
            day_of_week=6, location=Location.INPATIENT, start_time=7, end_time=17.5,
            caregiver_type=CaregiverType.RPH, skills=set()))

        # Saturday
        self.rph_template.append(Shift(
            day_of_week=7, location=Location.INPATIENT, start_time=7.5, end_time=16,
            caregiver_type=CaregiverType.RPH, skills=set()))

    def build_tech_template(self):
        # Sunday
        self.tech_template.append(Shift(
            day_of_week=1, location=Location.INPATIENT, start_time=7.5, end_time=16,
            caregiver_type=CaregiverType.TECH, skills=set()))

        # Monday
        self.tech_template.append(Shift(
            day_of_week=2, location=Location.RETAIL, start_time=7.5, end_time=16,
            caregiver_type=CaregiverType.TECH, skills=set()))
        self.tech_template.append(Shift(
            day_of_week=2, location=Location.RETAIL, start_time=8.5, end_time=17,
            caregiver_type=CaregiverType.TECH, skills=set()))
        self.tech_template.append(Shift(
            day_of_week=2, location=Location.RETAIL, start_time=9.5, end_time=18,
            caregiver_type=CaregiverType.TECH, skills=set()))
        self.tech_template.append(Shift(
            day_of_week=2, location=Location.INPATIENT, start_time=7, end_time=15.5,
            caregiver_type=CaregiverType.TECH, skills=set()))
        self.tech_template.append(Shift(
            day_of_week=2, location=Location.INPATIENT, start_time=9, end_time=17.5,
            caregiver_type=CaregiverType.TECH, skills=set()))

        # Tuesday
        self.tech_template.append(Shift(
            day_of_week=3, location=Location.RETAIL, start_time=7.5, end_time=16,
            caregiver_type=CaregiverType.TECH, skills=set()))
        self.tech_template.append(Shift(
            day_of_week=3, location=Location.RETAIL, start_time=8.5, end_time=17,
            caregiver_type=CaregiverType.TECH, skills=set()))
        self.tech_template.append(Shift(
            day_of_week=3, location=Location.RETAIL, start_time=9.5, end_time=18,
            caregiver_type=CaregiverType.TECH, skills=set()))
        self.tech_template.append(Shift(
            day_of_week=3, location=Location.INPATIENT, start_time=7, end_time=15.5,
            caregiver_type=CaregiverType.TECH, skills=set()))
        self.tech_template.append(Shift(
            day_of_week=3, location=Location.INPATIENT, start_time=9, end_time=17.5,
            caregiver_type=CaregiverType.TECH, skills=set()))

        # Wednesday
        self.tech_template.append(Shift(
            day_of_week=4, location=Location.RETAIL, start_time=7.5, end_time=16,
            caregiver_type=CaregiverType.TECH, skills=set()))
        self.tech_template.append(Shift(
            day_of_week=4, location=Location.RETAIL, start_time=8.5, end_time=17,
            caregiver_type=CaregiverType.TECH, skills=set()))
        self.tech_template.append(Shift(
            day_of_week=4, location=Location.RETAIL, start_time=9.5, end_time=18,
            caregiver_type=CaregiverType.TECH, skills=set()))
        self.tech_template.append(Shift(
            day_of_week=4, location=Location.INPATIENT, start_time=7, end_time=15.5,
            caregiver_type=CaregiverType.TECH, skills=set()))
        self.tech_template.append(Shift(
            day_of_week=4, location=Location.INPATIENT, start_time=9, end_time=17.5,
            caregiver_type=CaregiverType.TECH, skills=set()))

        # Thursday
        self.tech_template.append(Shift(
            day_of_week=5, location=Location.RETAIL, start_time=7.5, end_time=16,
            caregiver_type=CaregiverType.TECH, skills=set()))
        self.tech_template.append(Shift(
            day_of_week=5, location=Location.RETAIL, start_time=8.5, end_time=17,
            caregiver_type=CaregiverType.TECH, skills=set()))
        self.tech_template.append(Shift(
            day_of_week=5, location=Location.RETAIL, start_time=9.5, end_time=18,
            caregiver_type=CaregiverType.TECH, skills=set()))
        self.tech_template.append(Shift(
            day_of_week=5, location=Location.INPATIENT, start_time=7, end_time=15.5,
            caregiver_type=CaregiverType.TECH, skills=set()))
        self.tech_template.append(Shift(
            day_of_week=5, location=Location.INPATIENT, start_time=9, end_time=17.5,
            caregiver_type=CaregiverType.TECH, skills=set()))

        # Friday
        self.tech_template.append(Shift(
            day_of_week=6, location=Location.RETAIL, start_time=7.5, end_time=16,
            caregiver_type=CaregiverType.TECH, skills=set()))
        self.tech_template.append(Shift(
            day_of_week=6, location=Location.RETAIL, start_time=8.5, end_time=17,
            caregiver_type=CaregiverType.TECH, skills=set()))
        self.tech_template.append(Shift(
            day_of_week=6, location=Location.RETAIL, start_time=9.5, end_time=18,
            caregiver_type=CaregiverType.TECH, skills=set()))
        self.tech_template.append(Shift(
            day_of_week=6, location=Location.INPATIENT, start_time=7, end_time=15.5,
            caregiver_type=CaregiverType.TECH, skills=set()))
        self.tech_template.append(Shift(
            day_of_week=6, location=Location.INPATIENT, start_time=9, end_time=17.5,
            caregiver_type=CaregiverType.TECH, skills=set()))

        # Saturday
        self.tech_template.append(Shift(
            day_of_week=7, location=Location.INPATIENT, start_time=7.5, end_time=16,
            caregiver_type=CaregiverType.TECH, skills=set()))
