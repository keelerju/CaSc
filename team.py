class Team:
    """ Class representation of the team of caregivers """

    def __init__(self):
        self.team = []
        self.unassigned_members = []

    def build_team(self):
        pass

    def add_team_member(self, caregiver):
        self.team.append(caregiver)

    def remove_team_member(self, cg_id):
        t = []
        for e in self.team:
            if e.caregiver_id_num == cg_id:
                continue
            t.append(e)
        self.team = t

    def erase_team(self):
        self.team.clear()

    def roster(self):
        for person in self.team:
            print(vars(person))
