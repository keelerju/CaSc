from constraint import Constraint


class Constraints:
    """ Class representing a constraint for a specific date """

    def __init__(self):
        self.constraints = []

    def add_constraint(self, date, criteria, value):
        self.constraints.append(Constraint(date, criteria, value))

    def remove_constraint(self):
        self.list_constraints()
        index = int(input("Which constraint index is to be removed? "))
        del self.constraints[index]

    def list_constraints(self):
        index = 0
        for constraint in self.constraints:
            print(f"Index: {index}    {constraint}")
            index += 1
