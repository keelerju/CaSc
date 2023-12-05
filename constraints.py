from constraint import Constraint
from datetime import date
from conscrittype import ConsCritType


class Constraints:
    """ Class representing a constraint for a specific date """

    def __init__(self):
        self.constraints = []

    def add_constraints(self, team, rph_schedule, tech_schedule):
        # Accept constraints from the user and append them to the list of constraints
        repeat = True
        while repeat:
            _date = input("Please enter the date of a constraint in the format of MM/DD/YYYY: ")
            _date = date(int(_date[6:10]), int(_date[0:2]), int(_date[3:5]))

            print("**************************************")
            print("* 1 Caregiver cannot work this date  *")
            print("* 2 Caregiver must work this date    *")
            print("* 3 Shift requires chemo admixture   *")
            print("**************************************")
            _criteria = int(input("Please enter the criteria for the constraint: "))
            if _criteria == 3:
                pass

            if _criteria == 1:
                _caregiver_id_num = input("Please enter the value of the criteria: ")

            self.constraints.append(Constraint(date=_date, criteria=_criteria, caregiver_id_num=_caregiver_id_num))

    def remove_constraint(self):
        # Show an indexed list of constraints and have user choose a valid index to remove or [ENTER] to escape.
        self.list_constraints()
        index = 0
        valid = True
        while valid:
            index = int(input("Which constraint index is to be removed? (or hit [ENTER] to escape) "))
            if index == "":
                break
            if index not in range(1, (len(self.constraints) + 1)):
                print("Unknown constraint.  Please try again or hit [ENTER] to escape")
                continue
        del self.constraints[index - 1]

    def list_constraints(self):
        # Show an indexed list of constraints and pause after each page of results.
        index = 1
        page = 1
        length = len(self.constraints)
        for constraint in self.constraints:
            print(f"Index: {index}    {constraint}")
            index += 1
            if index % 20 == 0:
                input(f"Page {page} of {length}.  Press [ENTER] to continue.")
                page += 1
