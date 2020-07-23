import random

game_input = ['Null','x','O','x','O','x','O','x','O','x'];

def board(game_input):
    print('     |     |     ')
    print('  '+game_input[7]+'  |  '+game_input[8]+'  |  '+game_input[9])
    print('_____|_____|_____')
    print('     |     |     ')
    print('  '+game_input[4]+'  |  '+game_input[5]+'  |  '+game_input[6])
    print('_____|_____|_____')
    print('     |     |     ')
    print('  '+game_input[1]+'  |  '+game_input[2]+'  |  '+game_input[3])
    print('     |     |     ')


#board(game_input)
def player_input():

    marker = ''
    while marker !='X' and marker !='O':
        print("please enter (X , O ) ")
        marker = input("plese enter player 1 symbol : ")

    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')

#player_input();
'''player1,player2= player_input()
print(player1)
print(player2)'''

def put_marker(game_input,marker,position):
    game_input[position] = marker

def win(game_input,marker):
    return ((game_input[1]==game_input[2]==game_input[3]==marker) or
            (game_input[4] == game_input[5] == game_input[6] == marker) or
            (game_input[7] == game_input[8] == game_input[9] == marker) or
            (game_input[1] == game_input[4] == game_input[7] == marker) or
            (game_input[2] == game_input[5] == game_input[8] == marker) or
            (game_input[3] == game_input[6] == game_input[9] == marker) or
            (game_input[1] == game_input[5] == game_input[9] == marker) or
            (game_input[3] == game_input[5] == game_input[7] == marker))
def chose_player():
    player = random.randint(1,2)

    if player ==1:
        return 'Player 1 '
    else:
        return 'Player 2 '

# check for empty space
def space(game_input,position):
    return game_input[position] == ' '

# full bord check , where space is avilable or not

def full_board_check(game_input):
    for i in range(1,10):
        if space(game_input,i):
            return False
    return True

# player chosen marker placement
def player_choice(game_input):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space(game_input,position):
        position = int(input("Plese chose your position (1-9) : "))
    return position

#play again after anyone won the match

def play_again():
    choice = input("Would you like to Play again [Y/N] : ")
    return choice == 'Y'

# game machenism
while True:
    the_board = [' ']*10
    player_1,player_2 = player_input()
    print(player_1 + ' is player_1 sign')
    print(player_2 + ' is player_2 sign')

    turn = chose_player()
    print(turn + ' will play First')

    play_game = input('Are you ready to play [Y/N] ? : ')
    if play_game == 'Y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'player_1':
            board(the_board)
            position = player_choice(the_board)
            put_marker(the_board,player_1,position)

            if win(the_board,player_1):
                board(the_board)
                print('Player 1 has won the match')
                game_on = False

            else:
                if full_board_check(the_board):
                    board(the_board)
                    print('Game Tie')
                    game_on = False

                else:
                    turn = 'player_2'

        else:
            board(the_board)
            position = player_choice(the_board)
            put_marker(the_board, player_2, position)

            if win(the_board, player_2):
                board(the_board)
                print('Player 2 has won the match')
                game_on = False

            else:
                if full_board_check(the_board):
                    board(the_board)
                    print('Game Tie')
                    game_on = False

                else:
                    turn = 'player_1'



    if not play_again():
        break