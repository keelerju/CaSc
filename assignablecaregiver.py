class AssignableCaregiver:
    """ Class with attributes for the caregiver and the remaining hours of the week yet to be assigned.
        Use is temporary when assigning shifts, because remaining hours is not a permanent attribute
        of a caregiver. """

    def __init__(self, caregiver, remaining_hours):
        self.caregiver = caregiver
        self.remaining_hours = remaining_hours
