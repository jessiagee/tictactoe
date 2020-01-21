#!/usr/bin/env python
# coding: utf-8

'''
A tic tac toe game done for Complete Python Bootcamp
'''

import random

def display_board(board, marker = '', selection = 0):
    '''
    Display the tic tac toe board
    
    INPUT: board (list)
            marker (string)
            selection (int)

    OUTPUT: bool (False if someone has won, True otherwise)
    '''
    board[selection] = marker
    
    print(board[0] + '  |  ' + board[1] + '  |  ' + board[2] + '\n____________')
    print(board[3] + '  |  ' + board[4] + '  |  ' + board[5] + '\n____________') 
    print(board[6] + '  |  ' + board[7] + '  |  ' + board[8])   
    
    top_row = [board[0],board[1],board[2]]
    middle_row = [board[3],board[4],board[5]]
    bottom_row = [board[6],board[7],board[8]]

    left_col = [board[0],board[3],board[6]]
    middle_col = [board[1],board[4],board[7]]
    right_col = [board[2],board[5],board[8]]
    
    left_to_right = [board[0],board[4],board[8]]
    right_to_left = [board[2],board[4],board[6]]
    
    # if one of the rows or columns is filled, there is now a winner
    # so return 'False' for the no_winner check
    if check_rows_and_columns(bottom_row, middle_row, top_row, left_col, middle_col, right_col, left_to_right, right_to_left):
        return False
    else:
        return True

def check_rows_and_columns(*args):
    '''
    Checks the rows and columns for a winner
    
    INPUT: *args (eight lists for the rows, columns, and diagonols) 

    OUTPUT: bool (True if a row is full with the same marker, False otherwise)
    '''
    for row_col in args:
        # if there's only one item in the set for this row/col
        # and there's no empty spaces, the player has won
        if len(list(set(row_col))) == 1 and '' not in row_col:
            return True
    
    return False

def start_game():
    '''
    Starts the game after assigning players and markers
    '''
    player, player1_marker, other_player, player2_marker = assign_players_and_markers()
    
    run_game(player, other_player, player1_marker, player2_marker)

def run_game(first_player, second_player, first_player_marker, second_player_marker):
    '''
    Main code logic to run the game
    Allows players to replay if someone wins or there is a draw
    
    INPUT: first_player (string)
            second_player (string)
            first_player_marker (string)
            second_player_marker (string)
    '''
    # initial values for first run
    player = first_player
    marker = first_player_marker
    board = [''] * 9
    selected_nums = []
    no_winner = True
    
    display_board(board)
    
    # main game loop
    while (no_winner):
        selection = validate_selection(f"\n{player} place your marker using a number (1 - 9, left to right, top to bottom): ", selected_nums)
        
        no_winner = display_board(board, marker, selection)
        
        # no one has won yet
        if (no_winner == True):
            # if the entire board is filled but no one has won, it's a draw
            if '' not in board:
                print('\nThe game ends in a draw!')
                replay()
                break
            
            if player == first_player:
                player = second_player
                marker = second_player_marker
            else:
                player = first_player
                marker = first_player_marker
                
            no_num_selected = True
        # someone has won
        else:
            print(f'{player} wins!')
            replay()

def replay():
    '''
    Replays the game depending on player input
    '''
    user_input = 'Do you want to play again? [Y, N]: '
    valid_key_1 = 'Y'
    valid_key_2 = 'N'
    
    replay = validate_input(user_input, valid_key_1, valid_key_2)
    
    if replay == 'Y':
        start_game()
    else:
        exit()

def assign_players_and_markers():
    '''
    Randomly assigns which player goes first and allows 
    users to select their markers (X, O).
    
    OUTPUT: player (string)
            marker (string)
            other_player (string)
            other_marker (string)
    '''
    player = 'Player 1' if random.randint(1,2) == 1 else 'Player 2'
    
    user_input = f'{player} please pick a marker [X, O]: '
    valid_key_1 = 'X'
    valid_key_2 = 'O'
    
    marker = validate_input(user_input, valid_key_1, valid_key_2)
    
    if player == 'Player 1':
        other_player = 'Player 2'
        if marker == 'X':
            other_marker = 'O'
        else:
            other_marker = 'X'
    else:
        other_player = 'Player 1'
        if marker == 'X':
            other_marker = 'O'
        else:
            other_marker = 'X'
            
    return (player, marker, other_player, other_marker)
        
def validate_selection(selection, selected_nums):
    '''
    Validates the player's board selection to ensure that it is a 
    valid number within range.  Also checks that the player is 
    not trying to reuse an already selected position.
    
    INPUT: selection (int)
            selected_nums (list)
            
    OUTPUT: user_input (string)
    '''
    while True:
        try:
            user_input = int(input(selection))
            user_input -= 1
        except ValueError:
            print("Not a number! Try again.")
            continue
        else:
            while True:
                if (user_input < 0 or user_input > 8):
                    print("Out of range! Try again.")
                    break
                elif (user_input in selected_nums):
                    print(f'{user_input + 1} already used, pick another!')
                    break
                else:
                    selected_nums.append(user_input)
                    return user_input

def validate_input(user_input, valid_key_1, valid_key_2):
    '''
    Validates the player's input. 
    
    INPUT: user_input (string)
            valid_key_1 (string)
            valid_key_2 (string)
            
    OUTPUT: to_validate (string)
    '''
    to_validate = ''
    
    while True:
        to_validate = input(user_input)
        to_validate = to_validate.upper()
        
        if (to_validate == valid_key_1 or to_validate == valid_key_2):
            return to_validate
        else:
            print("Incorrect option! Try again.")
            continue
            
# entry point for the game      
start_game()




