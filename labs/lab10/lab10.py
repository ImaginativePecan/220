"""
Name: Jake Tanner
lab10.py
"""


def build_board():
    return ['1', '2', '3', '4', '5', '6', '7', '8', '9']


def display_board(board):
    print(str(board[0]) + '|' + str(board[1]) + '|' + str(board[2]))
    print('-----')
    print(str(board[3]) + '|' + str(board[4]) + '|' + str(board[5]))
    print('-----')
    print(str(board[6]) + '|' + str(board[7]) + '|' + str(board[8]))


def fill_spot(board, character):
    player_turn = character
    total_moves = 0
    updated_board = board
    for i in range(4):
        display_board(updated_board)
        print('It is player', player_turn + '\'s turn')
        attempt_place = input('please enter which position you want to place: ')

        while is_legal(updated_board, attempt_place):
            attempt_place = input('please enter a different position: ')

        if not is_legal(updated_board, attempt_place):
            position = attempt_place
            board[int(position) - 1] = player_turn
            total_moves += 1
            updated_board = board

        if player_turn == 'x':
            player_turn = 'o'
        elif player_turn == 'o':
            player_turn = 'x'

    return updated_board


def is_legal(board, attempt_place):
    if board[int(attempt_place) - 1] == 'x' or 'o':
        return False
    if board[int(attempt_place) - 1] == '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9':
        return True


def game_won():
    updated_board = (build_board(), 'x')
    # rows
    if updated_board[0] == updated_board[1] == updated_board[2] == 'x':
        print('Game Over')
        print('x won!')
        return True

    elif updated_board[4] == updated_board[5] == updated_board[6] == 'x':
        print('Game Over')
        print('x won!')
        return True

    elif updated_board[6] == updated_board[7] == updated_board[8] == 'x':
        print('Game Over')
        print('x won!')
        return True

    if updated_board[0] == updated_board[1] == updated_board[2] == 'o':
        print('Game Over')
        print('o won!')
        return True

    elif updated_board[4] == updated_board[5] == updated_board[6] == 'o':
        print('Game Over')
        print('o won!')
        return True

    elif updated_board[6] == updated_board[7] == updated_board[8] == 'o':
        print('Game Over')
        print('o won!')
        return True

    # columns
    elif updated_board[0] == updated_board[3] == updated_board[6] == 'x':
        print('Game Over')
        print('x won!')
        return True

    elif updated_board[1] == updated_board[4] == updated_board[7] == 'x':
        print('Game Over')
        print('x won!')
        return True

    elif updated_board[2] == updated_board[5] == updated_board[9] == 'x':
        print('Game Over')
        print('x won!')
        return True

    elif updated_board[0] == updated_board[3] == updated_board[6] == 'o':
        print('Game Over')
        print('o won!')
        return True

    elif updated_board[1] == updated_board[4] == updated_board[7] == 'o':
        print('Game Over')
        print('o won!')
        return True

    elif updated_board[2] == updated_board[5] == updated_board[8] == 'o':
        print('Game Over')
        print('o won!')
        return True

    elif updated_board[1] == updated_board[4] == updated_board[7] == 'x':
        print('Game Over')
        print('x won!')
        return True

    elif updated_board[1] == updated_board[4] == updated_board[7] == 'o':
        print('Game Over')
        print('o won!')
        return True

    # diagonal
    elif updated_board[2] == updated_board[4] == updated_board[6] == 'x':
        print('Game Over')
        print('x won!')
        return True

    elif updated_board[2] == updated_board[4] == updated_board[6] == 'o':
        print('Game Over')
        print('o won!')
        return True

    elif updated_board[0] == updated_board[4] == updated_board[8] == 'x':
        print('Game Over')
        print('x won!')
        return True

    elif updated_board[0] == updated_board[4] == updated_board[8] == 'o':
        print('Game Over')
        print('o won!')
        return True

    else:
        return False


def game_over():
    if fill_spot((build_board()), 'x') == 9:
        print('there are no more moves available')

    if game_won():
        print('the game was won')

    if not game_won():
        print('the game ended in a tie')


def play_game():
    while not game_over():
        fill_spot((build_board()), 'x')
        game_over()


def main():
    play_game()


main()
