from ui import inq_select
from ui import choose
from gui import gui
import game_assets
    

def create_character(country):

    # If there is no country, go back to menu
    if country == None:
        return None
    
    print('\033c')

    while True:
        game_assets.player['first_name'] = input("Enter a first name for your player character: ")
        game_assets.player['last_name'] = input('Enter a last name for your player character: ')
        
        try:
            game_assets.player['pronouns'] = game_assets.races[choose('Select pronouns for your player character:', game_assets.pronouns)]
        except:
            continue

        try:
            game_assets.player['race'] = game_assets.races[choose('Select a race for your player character:', game_assets.races)]
        except:
            continue

        game_assets.player['country'] = country

        party = ''
        options = []
        for party in country.parties:
            # IF party in ruling coalition, list it as such. IF NOT, list it as opposition
            if party in country.ruling_coalition:
                options.append(f"Ruling: {party.name} ({party.initials})")
            else:
                options.append(f'Opposition: {party.name} ({party.initials})')

        try:
            party = country.parties[choose("Select a party:", options)]
        except:
            break

        game_assets.player['party'] = party
        
        print(f'Name: {game_assets.player['first_name']} {game_assets.player['last_name']}')
        print(f'Pronouns: {game_assets.player['pronouns']}')
        print(f'Race: {game_assets.player['race']}')
        print(f'Country: {game_assets.player['country'].name}')
        print(f'Party: {game_assets.player['party'].name}')
        match inq_select(f"Confirm this as your player character: ", 'Deny', 'Confirm'):
            case 1:
                continue
            case 2:
                gui()
                break

def inspect_party(party):

    while True:
        print('\033c')
        print(party)

        match inq_select('Select an action:', 'Inspect Party Leader', 'Back'):
            case 1:
                print('\033c')
                print(party.party_leader)
                input('\nEnter anything to continue: ')
            case 2:
                print('\033c')
                break

def select_country(country):
    while True:
        print('\033c')
        print(country)

        choice = inq_select('Select an action:', 'Read Political Situation', "Inspect Parties", "Select This Country", 'Back')

        match choice:
            case 1:
                print('\033c')
                print(f"{country.name}'s Political Situation:\n")
                print(country.description)
                input('Enter anything to continue: ')
            case 2:
                print('\033c')
                options = []
                for party in country.parties:
                    if party in country.ruling_coalition:
                        options.append(f"Ruling: {party.name} ({party.initials})")
                    else:
                        options.append(f'Opposition: {party.name} ({party.initials})')

                try:
                    party = country.parties[choose("Select a party:", options)]
                    inspect_party(party)
                except:
                    continue
            case 3:
                match inq_select(f"Confirm that you want to select {country.name} as your country: ", 'Deny', 'Confirm'):
                    case 1:
                        continue
                    case 2:
                        return country
            case 4:
                print('\033c')
                return None
                
def game_set_menu():
    print('\033c')

    while True:
        country = inq_select("Select a country:", 'Republic of Aoranias')

        match country:
            case 1:
                create_character(select_country(game_assets.aorania))
        continue

