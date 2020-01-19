#!/usr/bin/env python
# coding: utf-8

# In[56]:


def display_board(board, player = '', selection = 0):
    board[selection] = player
    
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
    for row_col in args:
        # if there's only one item in the set for this row/col
        # and there's no empty spaces, the player has won
        if len(list(set(row_col))) == 1 and '' not in row_col:
            return True
    
    return False

def start_game():
    player1 = validate_player()
    
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    
    print(f'\nPlayer 1 is {player1} and player 2 is {player2}! \nPlayer 1 goes first!')
    
    run_game(player1, player2)

def run_game(player1, player2):
    player = player1
    board = []
    selected_num = []
    no_winner = True
    
    display_board(board)
    
    while (no_winner):
        selection = validate_selection(f"\n{player} place your marker using a number (1 - 9, left to right, top to bottom): ", selected_num)
        
        no_winner = display_board(board, player, selection)
        
        if (no_winner == True):
            if '' not in board:
                print('\nThe game ends in a draw!')
                replay()
                break
            
            if player == player1:
                player = player2
            else:
                player = player1
                
            no_num_selected = True
        else:
            print(f'{player} wins!')
            replay()

def replay():
    replay = validate_replay()
    
    if replay == 'Y':
        start_game()
    else:
        exit()
                
def validate_selection(selection, selected_num):
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
                elif (user_input in selected_num):
                    print(f'{user_input} already used, pick another!')
                    break
                else:
                    selected_num.append(user_input)
                    return user_input

def validate_player():    
    while True:
        player = input("\nPlayer 1 please pick a marker [X, O]: ")
        player = player.upper()
        
        if player == "X" or player == "O":
            return player
        else:
            print("Incorrect player option! Try again.")
            continue

def validate_replay():    
    while True:
        replay = input(f'\nDo you want to play again? [Y, N]')
        replay = replay.upper()
        
        if replay == "Y" or replay == "N":
            return replay
        else:
            print("Incorrect replay option! Try again.")
            continue            
            
start_game()


# In[ ]:





# In[ ]:




