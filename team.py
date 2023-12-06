from caregiver import Caregiver
from caregivertype import CaregiverType


class Team:
    """ Class representation of the team of caregivers """

    def __init__(self):
        self.team = []
        self.unassigned_members = []

    def build_team(self, team_size):
        for index, _caregiver in enumerate(range(team_size)):
            name = input("Please enter caregiver name: ")
            caregiver_id_num = input("Please enter caregiver ID number: ")
            caregiver_type = input("Please enter caregiver type: ")
            min_hours = input("Please enter hours per pay period: ")
            self.add_team_member(Caregiver(name=name, caregiver_id_num=caregiver_id_num,
                                           caregiver_type=CaregiverType(caregiver_type), min_hours=min_hours))
            print(f"*** Caregiver # {index + 1} of {team_size} added to team ***\n")

    def add_team_member(self, caregiver):
        self.team.append(caregiver)

    def edit_team_member(self, caregiver_id_num):
        pass

    def remove_team_member(self, cg_id):
        _team = []
        for _caregiver in self.team:
            if _caregiver.caregiver_id_num == cg_id:
                continue
            _team.append(_caregiver)
        self.team = _team

    def erase_team(self):
        self.team.clear()

    def roster(self):
        for _caregiver in self.team:
            print(vars(_caregiver))
