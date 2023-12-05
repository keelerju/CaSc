from constraint import Constraint


class Constraints:
    """ Class representing a constraint for a specific date """

    def __init__(self):
        self.constraints = []

    def add_constraint(self, _date, _criteria, _employee_id_num):
        self.constraints.append(Constraint(date=_date, criteria=_criteria, employee_id_num=_employee_id_num))

    def remove_constraint(self):
        # Show an indexed list of constraints and have user choose a valid index to remove or [ENTER] to escape.
        self.list_constraints()
        index = 0
        valid = True
        while valid:
            index = int(input("Which constraint index is to be removed? (or hit [ENTER] to escape) "))
            if index == "":
                break
            if index not in range(0, index):
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
