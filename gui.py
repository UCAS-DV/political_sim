import math
import game_assets
from ui import inq_select

def set_title(country, party, pronouns, last_name):
    if country.political_system == 'Parliamentary':
        if party in country.ruling_coalition:
            return "Prime Minister " + last_name
        else:
            match pronouns:
                case 'He/Him':
                    return "Mr. " + last_name
                case 'She/Her':
                    return "Ms. " + last_name
                case 'They/Them':
                    return '' + last_name

def gui():
    print('\033c')
    month = 0
    year = math.floor(month / 12) + 1

    player_country = game_assets.player['country']
    player_last_name = game_assets.player['last_name']
    player_party = game_assets.player['party']
    player_pronouns = game_assets.player['pronouns']

    while True:
        
        print(f'Month: {(month - (12 * (year-1))) + 1}')
        print(f'Year: {year}')

        match inq_select(f'{set_title(player_country, player_party, player_pronouns, player_last_name)}, what should we do?', 'Check Major Issues', 'Pass Month'):
            case 1:
                print('\033c')
                print(f'{player_country.name} Issues \n')
                for issue in player_country.issues:
                    print(f'{issue}\n')
                input('Enter to continue: ')
            case 2:
                print('\033c')
                month += 1
                year = math.floor(month / 12) + 1

gui()