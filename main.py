dash = '-'
wall = ' | '
game = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


def positions():
    for index, words in enumerate(game):
        if index == 0 or index == 3 or index == 6:
            print(index+1, wall, index + 2, wall, index + 3)
        if index == 0 or index == 3:
            print(dash * 15)

    print('These are the Positions of the game ☝️\n\n')


positions()


def winner_check(game):
    if game[0] == game[1] == game[2] and game[0] != ' ':
        return True
    elif game[3] == game[4] == game[5] and game[3] != ' ':
        return True
    elif game[6] == game[7] == game[8] and game[6] != ' ':
        return True
    elif game[0] == game[4] == game[8] and game[0] != ' ':
        return True
    elif game[2] == game[4] == game[6] and game[2] != ' ':
        return True
    elif game[0] == game[3] == game[6] and game[0] != ' ':
        return True
    elif game[1] == game[4] == game[7] and game[1] != ' ':
        return True
    elif game[2] == game[5] == game[8] and game[2] != ' ':
        return True
    else:
        return False


def live_game():
    for index, words in enumerate(game):
        if index == 0 or index == 3 or index == 6:
            print(game[index], wall, game[index + 1], wall, game[index + 2])
        if index == 0 or index == 3:
            print(dash * 15)


live_game()
print("\n")
n = 0
game_going_On = True
while game_going_On:
    if n % 2 == 0:
        user_input = int(input("player 1, where's your move, from(1,9)? : "))
        if user_input in range(0, 11) and game[user_input - 1] == ' ':
            game[user_input - 1] = "X"
            n += 1
            live_game()
            print("\n")
        else:
            print("you have enter wrong move, please check the positions and enter your position from 1,9")

        result = winner_check(game)

        if result == bool(True):
            print(f" Player 1 !!! Whoa you won")
            game_going_On = False
        else:
            pass
    elif n % 2 != 0:
        p2_user_input = int(input("player 2, where's your move, from(1,9)? : "))
        if p2_user_input in range(0, 11) and game[p2_user_input - 1] == ' ':
            game[p2_user_input - 1] = 'O'
            n += 1
            live_game()
            print("\n")
        else:
            print("you have enter wrong move, please check the positions and enter your position from 1,9")

        result = winner_check(game)
        if result == bool(True):
            print(f" Player 2 !!! Whoa you won")
            game_going_On = False

    if " " not in game:
        print('Match Tie')
        game_going_On = False
