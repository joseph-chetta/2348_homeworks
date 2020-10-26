# Joseph Chetta 1640405

def print_menu():
    print('MENU')
    print('a - Add player')
    print('d - Remove player')
    print('u - Update player rating')
    print('r - Output players above a rating')
    print('o - Output roster')
    print('q - Quit\n')

def menu_options(players):
    print()
    print_menu()
    option = None
    while option != 'q':
        option = input('Choose an option:\n')
        if option == 'q':
            break
        elif option == 'a':
            jersey_num = int(input("Enter a new player's jersey number:"))
            rating = input("Enter the player's rating:")
            players[jersey_num] = rating
            print_menu()
        elif option == 'd':
            jersey_num = int(input("Enter a jersey number:"))
            del players[jersey_num]
            print_menu()
        elif option == 'u':
            jersey_num = int(input("Enter a jersey number:"))
            rating = input("Enter a new rating for player:")
            players[jersey_num] = rating
            print_menu()
        elif option == 'r':
            min_rating = input("Enter a rating:\n")
            print('ABOVE {}'.format(min_rating))
            for i in sorted(players):
                if players[i] > min_rating:
                    print('Jersey number: {}, Rating: {}'.format(i, players[i]))
            print()
            print_menu()
        elif option == 'o':
            print('ROSTER')
            for i in sorted(players):
                print('Jersey number: {}, Rating: {}'.format(i, players[i]))
            print()
            print_menu()



if __name__ == '__main__':
    # key is jersey number
    # rating is field value
    players = {}
    for i in range(1, 6):
        jersey_num = int(input("Enter player {}'s jersey number:\n".format(i)))
        rating = input("Enter player {}'s rating:\n".format(i))
        print()
        players[jersey_num] = rating

    print('ROSTER')
    for i in sorted(players):
        print('Jersey number: {}, Rating: {}'.format(i, players[i]))

    menu_options(players)
