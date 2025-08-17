from ui import inq_select
from game_set import game_set_menu

def main():
    game_title = "Fantasy Political Simulator"

    while True:
        print("\n" + "=" * 60)
        print(f"{game_title.center(60)}")
        print("A text-based political simulator by Darius".center(60))
        print("=" * 60)

        choice = inq_select('Use the arrow keys and "Enter" to navigate UI.', 'New Game', 'Load Game', 'Exit')

        match choice:
            case 1:
                game_set_menu()
            case 3:
                print("Thanks for playing!")
                break


main()