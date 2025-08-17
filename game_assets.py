import math


class country:
    def __init__(self, name, description, executive, opposition_leader, parties, ruling_coalition, political_system, issues, money_available, lower_seats, upper_seats):
        self.name = name
        self.description = description

        self.executive = executive
        self.opposition_leader = opposition_leader

        self.parties = parties
        self.ruling_coalition = ruling_coalition

        for party in self.parties:
            party.country = self

        self.political_system = political_system

        if self.political_system == "Parliamentary":
            executive.position == "Prime Minister"
    
        opposition_leader.position = "Opposition Leader"

        self.issues = issues
        self.money_available = money_available

        self.lower_seats = lower_seats
        self.upper_seats = upper_seats

    def __str__(self):

        country_string = f"Country: {self.name}\nPolitical System: {self.political_system}\n\n"

        if self.political_system == "Parliamentary":
            country_string += f"Prime Minister: {self.executive.name} - {self.executive.race} - {self.executive.party.initials}\n"

        country_string += f"Leader of the Opposition: {self.opposition_leader.name} - {self.opposition_leader.race} - {self.opposition_leader.party.initials}\n\n"
        country_string += f"Ruling Coalition:\n"
        
        for party in self.ruling_coalition:
            country_string += f"    {party.name} - {party.initials} - {party.general_alignment}\n"
        
        country_string += f"\nOpposition Parties:\n"

        for party in self.parties:

            # IF party is not in ruling coalition, list party as opposition
            if party not in self.ruling_coalition:
                country_string += f"    {party.name} - {party.initials} - {party.general_alignment}\n\n"

        if self.money_available > 0:
            country_string += f"O${self.money_available}M Surplus\n"
        else:
            country_string += f"O${self.money_available * -1}M Debt\n"

        if self.political_system == "Parliamentary":

            country_string += f"\nParliament - {self.lower_seats} Total Seats "

            # Calculating the seats needed for a majority based on whether there's an even or odd number of seats
            if self.lower_seats % 2 == 0:
                country_string +=  f"- {math.ceil(self.lower_seats/2) + 1} Seats Needed For Majority:\n"
            else:
                country_string +=  f"- {math.ceil(self.lower_seats/2)} Seats Needed For Majority:\n"

            for party in self.parties:
                country_string += f'    {party.initials} - {party.lower_seats} seats\n'

        return country_string

class party:
    def __init__(self, name, initials, party_leader, general_alignment, economic_alignment, social_alignment, foreign_alignment, lower_seats, upper_seats):
        self.name = name
        self.initials = initials
        self.party_leader = party_leader
        self.country = "TBD"

        party_leader.party = self

        self.general_alignment = general_alignment
        self.economic_alignment = economic_alignment
        self.social_alignment = social_alignment
        self.foreign_alignment = foreign_alignment

        self.lower_seats = lower_seats
        self.upper_seats = upper_seats

    def __str__(self):

        party_string = f"Party: {self.name} - {self.initials}\n\nParty Leader: {self.party_leader.name} ({self.party_leader.race})\n\nGeneral Alignment: {self.general_alignment}\n\n"
        
        # Economic Alignment
        economic_string = "Economic Alignment: "
        if -1 < self.economic_alignment < 1:
            economic_string += "Centre\n"
        elif -3 < self.economic_alignment <= -1:
            economic_string += "Centre-Left\n"
        elif -5 < self.economic_alignment <= -3:
            economic_string += "Left\n"
        elif -7 < self.economic_alignment <= -5:
            economic_string += "Far Left\n"
        elif 1 <= self.economic_alignment < 3:
            economic_string += "Centre-Right\n"
        elif 3 <= self.economic_alignment < 5:
            economic_string += "Right\n"
        elif 5 <= self.economic_alignment < 7:
            economic_string += "Far Right\n"
        
        # Social Alignment
        social_string = "Social Alignment: "
        if -1 < self.social_alignment < 1:
            social_string += "Centre\n"
        elif -3 < self.social_alignment <= -1:
            social_string += "Centre-Left\n"
        elif -5 < self.social_alignment <= -3:
            social_string += "Left\n"
        elif -7 < self.social_alignment <= -5:
            social_string += "Far Left\n"
        elif 1 <= self.social_alignment < 3:
            social_string += "Centre-Right\n"
        elif 3 <= self.social_alignment < 5:
            social_string += "Right\n"
        elif 5 <= self.social_alignment < 7:
            social_string += "Far Right\n"

        # Foreign Alignment (can extend same logic if desired)
        foreign_string = f"Foreign Alignment: {self.foreign_alignment}\n"

        seat_string = ""
        if self.country.political_system == "Parliamentary":
            seat_string = f"\nParliamentary Seats: {self.lower_seats}"


        return party_string + economic_string + social_string + foreign_string + seat_string

class person:
    def __init__(self, name, race, party, general_alignment, economic_alignment, social_alignment, foreign_alignment, position):
        self.name = name

        self.last_name = name.split()[len(name.split()) - 1]

        self.race = race     
        self.party = party

        self.general_alignment = general_alignment
        self.economic_alignment = economic_alignment
        self.social_alignment = social_alignment
        self.foreign_alignment = foreign_alignment

        self.position = position

    def __str__(self):
        person_string = f"Person: {self.name}\nRace: {self.race}\n\nParty: {self.party.name}\n\nPosition: {self.position}\n\n"
        
        # Economic Alignment
        economic_string = "Economic Alignment: "
        if -1 < self.economic_alignment < 1:
            economic_string += "Centre\n"
        elif -3 < self.economic_alignment <= -1:
            economic_string += "Centre-Left\n"
        elif -5 < self.economic_alignment <= -3:
            economic_string += "Left\n"
        elif -7 < self.economic_alignment <= -5:
            economic_string += "Far Left\n"
        elif 1 <= self.economic_alignment < 3:
            economic_string += "Centre-Right\n"
        elif 3 <= self.economic_alignment < 5:
            economic_string += "Right\n"
        elif 5 <= self.economic_alignment < 7:
            economic_string += "Far Right\n"

        # Social Alignment
        social_string = "Social Alignment: "
        if -1 < self.social_alignment < 1:
            social_string += "Centre\n"
        elif -3 < self.social_alignment <= -1:
            social_string += "Centre-Left\n"
        elif -5 < self.social_alignment <= -3:
            social_string += "Left\n"
        elif -7 < self.social_alignment <= -5:
            social_string += "Far Left\n"
        elif 1 <= self.social_alignment < 3:
            social_string += "Centre-Right\n"
        elif 3 <= self.social_alignment < 5:
            social_string += "Right\n"
        elif 5 <= self.social_alignment < 7:
            social_string += "Far Right\n"

        # Foreign Alignment (can extend same logic if desired)
        foreign_string = f"Foreign Alignment: {self.foreign_alignment}"

        return person_string + economic_string + social_string + foreign_string
     
class issue:
    def __init__(self, name, description, criteria_func, criteria_display_func):
        self.name = name
        self.description = description
        self.criteria_func = criteria_func
        self.criteria_display_func = criteria_display_func
        self.resolved = False

    def check_resolved(self, criteria):
        self.resolved = self.criteria_func(criteria)
        return self.resolved
    
    def __str__(self):
        issue_string = f"Issue: {self.name}\nDescription: {self.description}\nCriteria: {self.criteria_display_func()}"

        if self.resolved:
            issue_string += '\nStatus: Resolved'
        else:
            issue_string += '\nStatus: Unresolved'

        return issue_string

# =================== People ===================
osvaria_pm = person(name="Sylvara Dewlight", race="Elf", party="Party Leader", general_alignment="Centre-Left",economic_alignment=-2,social_alignment=-3,foreign_alignment="Internationalist", position="Prime Minister")
ocp_leader = person("Andrew Stevens", "Human", party="Party Leader", general_alignment="Right", economic_alignment=3, social_alignment=5, foreign_alignment="Isolationist", position="Opposition Leader")

# =================== People ===================
osvarian_reform_party = party("Osvarian Reform Party", "ORP", osvaria_pm, "Centre-Left", -2, -2, "Internationalist", 54, 0)
osvarian_conservatives = party("Conservative Party of Osvaria", "CPO", ocp_leader, "Right", 3, 3, "Isolationist", 46, 0) 

# =================== Political Situations ===================

# PS stands for Political Situation

# Reads the political situation file
def read_ps(ps_filepath):
    with open(ps_filepath, 'r') as ps_file:
        return ps_file.read()

# =================== Criteria ===================
veterans = 200000
veterans_compensated = 90000

# =================== Criteria Functions ===================

def check_veteran_compensation():
    if veterans_compensated/veterans < 0.7:
        return False
    else:
        return True
    
def show_veteran_compensation():
    return f"{veterans_compensated/veterans * 100:.1f}% of veterans are compensated. 75% of veterans need to be compensated to resolve the issue."

# =================== Issues ===================
veterans_compensated_issue = issue('Veterans are uncompensated for their service', 'Test', check_veteran_compensation, show_veteran_compensation)

# =================== Countries ===================
osvaria = country("Western Osvarian Republic", read_ps('political_situations\osvarian_ps.txt'), 
                  osvaria_pm, ocp_leader, 
                  [osvarian_reform_party, osvarian_conservatives], [osvarian_reform_party], "Parliamentary", 
                  [veterans_compensated_issue], -70,
                  100, 0)

print(osvaria)

races = ['Human', 'Elf']
pronouns = ['He/Him', 'She/Her', 'They/Them']
player = {
    'first_name': 'Darius',
    'last_name': 'Vaiaoga',
    'race': 'Human',
    'pronouns': 'He/Him',
    'country': osvaria,
    'party': osvarian_reform_party
}