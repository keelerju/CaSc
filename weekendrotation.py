from datetime import date
from caregivertype import CaregiverType


class WeekendRotation:
    """ Class containing the weekend rotations of all caregivers,
    and useful attributes such as the reference date of a regularly
    scheduled Saturday of the start of RPh and Tech weekend rotations,
    and the number of caregivers who have regular weekend assignments """

    def __init__(self, team, rph_weekends=None, tech_weekends=None, ref_date_rph=None, ref_date_tech=None):

        self.team = team

        if not rph_weekends:
            self.set_rph_weekends()
        else:
            self.rph_weekends = rph_weekends

        if not tech_weekends:
            self.set_tech_weekends()
        else:
            self.tech_weekends = tech_weekends

        if not ref_date_rph:
            self.set_ref_date_rph()
        else:
            self.ref_date_rph = ref_date_rph

        if not ref_date_tech:
            self.set_ref_date_tech()
        else:
            self.ref_date_tech = ref_date_tech

        self.weekend_rph_count = len(rph_weekends)
        self.weekend_tech_count = len(tech_weekends)

    def set_rph_weekends(self):
        """ Print all RPh caregivers of the team, who are not per-diem and have set weekends,
         and allow the user to assign the order of the weekend rotation. """

        self.rph_weekends = []

        print("Pharmacist roster: ")
        rph_count = 0
        for caregiver in self.team:
            if caregiver.caregiver_type == CaregiverType.RPH and caregiver.min_hours:
                print(f"Caregiver ID: {caregiver.caregiver_id_num}    Name: {caregiver.name}")
                rph_count += 1

        for index in range(rph_count):
            print(f"Please enter the Caregiver ID of Pharmacist assigned to work weekend # {index}? ")
            self.rph_weekends.append(self.team[index])

    def set_tech_weekends(self):
        """ Print all Technician caregivers of the team, who are not per-diem and have set weekends,
                 and allow the user to assign the order of the weekend rotation. """

        self.rph_weekends = []

        print("Technician roster: ")
        tech_count = 0
        for caregiver in self.team:
            if caregiver.caregiver_type == CaregiverType.TECH and caregiver.min_hours:
                print(f"Caregiver ID: {caregiver.caregiver_id_num}    Name: {caregiver.name}")
                tech_count += 1

        for index in range(tech_count):
            print(f"Please enter the Caregiver ID of Technician assigned to work weekend # {index}? ")
            self.rph_weekends.append(self.team[index])

    def set_ref_date_rph(self):
        """ Set a reference date to establish the start of the repeating weekend rotation.
        The reference date may be a date in the past or future. """

        ref_date = input(f"Please enter a past or future date for when RPh Caregiver {self.rph_weekends[0].name} "
                         f"did work or will work a regularly scheduled Saturday in the format MM/DD/YYYY: ")

        self.ref_date_rph = date(int(ref_date[6:10]), int(ref_date[0:2]), int(ref_date[3:5]))

    def set_ref_date_tech(self):
        """ Set a reference date to establish the start of the repeating weekend rotation.
        The reference date may be a date in the past or future. """

        ref_date = input(f"Please enter a past or future date for when Tech Caregiver {self.tech_weekends[0].name} "
                         f"did work or will work a regularly scheduled Saturday in the format MM/DD/YYYY: ")

        self.ref_date_tech = date(int(ref_date[6:10]), int(ref_date[0:2]), int(ref_date[3:5]))
