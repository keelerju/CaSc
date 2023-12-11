from datetime import date
from caregivertype import CaregiverType


class WeekendRotation:
    """ Class containing the weekend rotations of all caregivers """

    def __init__(self, team, rph_weekends=None, tech_weekends=None, ref_date=None):

        self.team = team

        if not rph_weekends:
            self.set_rph_weekends()
        else:
            self.rph_weekends = rph_weekends

        if not tech_weekends:
            self.set_tech_weekends()
        else:
            self.tech_weekends = tech_weekends

        if not ref_date:
            self.set_ref_date()
        else:
            self.ref_date = ref_date

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

    def set_ref_date(self):
        """ Set a reference date to establish the start of the weekend rotation. """

        ref_date = input(f"Please enter a past or future date for when Caregiver {self.rph_weekends[0].name} "
                         f"did work or will work a regularly scheduled Saturday in the format MM/DD/YYYY: ")

