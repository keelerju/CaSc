class AssignableCaregiver:
    """ Class with attributes for the caregiver and the remaining hours of the week yet to be assigned.
        Similar to Team class, but use is temporary when assigning shifts.  """

    def __init__(self, caregiver, remaining_hours):
        self.caregiver = caregiver
        self.remaining_hours = remaining_hours
