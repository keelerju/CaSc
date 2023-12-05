# Program writes repeating schedules for Pharmacy caregivers
# that will identify and resolve issues such as:
#     Requirements: shift patterns, caregiver preferences, legal requirements
#     Caregiver Data: caregiver availability, skills, preferences
#     Scheduling Rules: maximum working hours, break times, relevant policies
#     Algorithm factors: fairness, workload distribution, caregiver satisfaction
#     Conflict management: overlapping shifts, exceeding maximum hours

from caregiver import Caregiver
from schedule import Schedule
from rphmonth import RphMonth
from techmonth import TechMonth
from team import Team
from datetime import date
from constraints import Constraints


def main():

    team = Team()
    team_size = int(input("Enter the number of caregivers: "))

    # # Create a team of caregivers, one having a specific caregiver id #, and the rest being default, print the roster,
    # # then remove the team member with custom caregiver id #, print roster again, then erase the team.
    for cg in range(team_size-1):
        cg = Caregiver()
        team.add_team_member(cg)
    team.add_team_member(Caregiver(caregiver_id_num=1111111))
    team.roster()
    print()
    team.remove_team_member(1111111)
    team.roster()
    team.erase_team()
    # # end of test

    month = int(input("\nWhich month is being created (1-12)? "))
    year = int(input("Of which year? "))

    schedule = Schedule(year, month)

    first_pay = int(input("\nThe 1st of this month is in week 1 or 2 of the pay period? "))
    print(f"Week {first_pay} of pay period\n")

    holidays = []
    while True:
        print(f"\nStarting with the Sunday of the week including the 1st of month {month},")
        print(f"and ending with the Saturday of the week including the last day of month {month},")
        holiday = input(f"please enter the date of a holiday in the format of MM/DD/YYYY, or ENTER for none. ")
        if not holiday:
            break
        else:
            holiday = date(int(holiday[6:10]), int(holiday[0:2]), int(holiday[3:5]))
            holidays.append(holiday)

    rph_month = RphMonth(year, month)
    rph_month.fill_blank(schedule.template.rph_template, holidays)
    rph_month.print_schedule()
    # rph_month.fill_must()
    # rph_month.random_assign(schedule.shifts.rph_shifts)

    tech_month = TechMonth(year, month)
    tech_month.fill_blank(schedule.template.tech_template, holidays)
    tech_month.print_schedule()
    # tech_month.fill_must()
    # tech_month.random_assign(schedule.shifts.tech_shifts)

    constraints = Constraints()

    cont = input("Are there any date constraints to add to the schedule for caregivers or shifts (Y/N)? ")
    if (cont == "N") or (cont == "n") or (cont == "no") or (cont == "NO") or (cont == "No"):
        pass
    else:
        constraints.add_constraints(team, rph_month.rph_schedule, tech_month.tech_schedule)


if __name__ == '__main__':
    main()
