from random import choice

grid = {1: ' ',2: ' ',3: ' ', 4: ' ',5: ' ',6: ' ', 7: ' ',8: ' ',9: ' '}

def print_help():
    print("Use a number to select your spot:")
    print()
    print(" 1 | 2 | 3 ")
    print("---|---|---")
    print(" 4 | 5 | 6 ")
    print("---|---|---")
    print(" 7 | 8 | 9 ")
    print()

def print_grid():
    print()
    print(f" {grid[1]} | {grid[2]} | {grid[3]} ")
    print("---|---|---")
    print(f" {grid[4]} | {grid[5]} | {grid[6]} ")
    print("---|---|---")
    print(f" {grid[7]} | {grid[8]} | {grid[9]} ")
    print()


def check_for_win(player):
    win = player * 3
    # iterate over rows and columns
    # check rows
    if f"{grid[1]}{grid[2]}{grid[3]}" == win:
        return True
    if f"{grid[4]}{grid[5]}{grid[6]}" == win:
        return True
    if f"{grid[7]}{grid[8]}{grid[9]}" == win:
        return True
    # check columns
    if f"{grid[1]}{grid[4]}{grid[7]}" == win:
        return True
    if f"{grid[2]}{grid[5]}{grid[8]}" == win:
        return True
    if f"{grid[3]}{grid[6]}{grid[9]}" == win:
        return True
    # check top left to bottom right diagonal
    if f"{grid[1]}{grid[5]}{grid[9]}" == win:
        return True
    # check top right to bottom left diagonal
    if f"{grid[3]}{grid[5]}{grid[7]}" == win:
        return True
    # if no spots remain, game over
    if not ' ' in grid.values():
        return 'GAME OVER'
    # next round
    return False


def computer_round():
    print("Computer's turn")
    empty_spots = []
    for key, value in grid.items():
        if value == ' ':
            empty_spots.append(key)
    if len(empty_spots) == 0:
        return 'GAME OVER'
    grid[choice(empty_spots)] = 'O'


# start game play
print_help()
game_over = False
game_round = 1
while not game_over == True:
    # odd round, player's turn, even round, computer's turn
    if game_round % 2 != 0:
        selection_valid = False
        selected_spot = ''
        while not selection_valid:
            selected_spot = int(input("Pick your spot (1-9): "))
            if 0 < selected_spot < 10 and grid[selected_spot] == ' ':
                selection_valid = True
            else:
                print('Selected spot is either taken or does not exist!')
        grid[selected_spot] = 'X'
        game_over = check_for_win('X')
        if game_over == True:
            print_grid()
            print('YOU WIN!')
        else:
            print_grid()
    else:
        computer_round()
        game_over = check_for_win('O')
        if game_over == True:
            print_grid()
            print('COMPUTER WINS, YOU LOSE!')
        else:
            print_grid()
    game_round = game_round + 1

if game_over == 'GAME OVER':
    print('GAME OVER - TIE')

