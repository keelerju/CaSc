from datetime import date


class WeekendRotation:
    """ Class containing the weekend rotations of all caregivers """
   
    def __init__(self, team, rph_rotation=None, tech_rotation=None, reference_date=None):
     
        self.team = team
   
        if rph_rotation == None:
            self.set_rph_rotation()
        else:
            self.rph_rotation = rph_rotation
        if tech_rotation == None:
            self.tech_rotation()
        else:
            self.tech_rotation = tech_rotation
        if reference_date == None:
            self.set_reference_date()
        else:
            self.reference_date = reference_date
   
   def set_rph_rotation():
       pass
      
   def set_tech_rotation():
       pass

   def set_reference_date():
       pass
