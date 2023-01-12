'''
Alan Preciado
02/20/2019

Below is a set of steps for you to follow to try to create the Tic Tac Toe Milestone Project game!
'''

from IPython.display import clear_output
import random


def display_board(board):
    clear_output()
    print('---------')
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('---------')


def player_input():
    marker = " "
    
    while marker != 'X' and marker != 'O':
        marker = input("Player 1 pick a marker 'X' or 'O': ")
        
    player1 = marker
    
    if player1 == 'X':
        player2 = 'O'
    
    else:
        player2 = 'X'
    
    return (player1, player2)


def place_marker(board, marker, position):
    # we'll rewrite the board list
    # not verifying each input --> assume they are correct 
    board[position] = marker
    return board

def win_check(board, mark):
    # define all winning configurations
    diagonal_1 = (1,5,9)
    diagonal_2 = (3,5,7)

    column_1 = (1,4,7)
    column_2 = (2,5,8)
    column_3 = (3,6,9)

    row_1 = (1,2,3)
    row_2 = (4,5,6)
    row_3 = (7,8,9)
    
    # check win by looping over rows, columns and diagonals
    for row in [row_1,row_2,row_3, column_1, column_2, column_3, diagonal_1, diagonal_2]:
        isWin = True
        for pos in row:
            #print(board[pos])
            if not board[pos] == mark: #must fulfill the three elements
                isWin = False
                #print(isWin)
                break
            
        if isWin:
            #print(row)
            return True
            #return row
        
    #print(row)       
    return False


def choose_first():
    if random.randint(1,2) == 1:
        return 'Player 1'
    else:
        return 'Player 2'


def space_check(board, position):
    #if board[position] != 'X' or board[position] != 'O': #check free space
    if board[position] == ' ':
        return True
    else:
        return False

def full_board_check(board):
    # assume empty space will ALWAYS have form ' '
    empty_space = ' '
    if empty_space in board:
        return False #board not full
    else:
        return True

def player_choice(board, player_in_turn):
    # Using while until player chooses empty space
    while True:
        position = int(input('{} please enter your position: '.format(player_in_turn)))
        
        if space_check(board,position):
            return position
            #break
        
        else:
            print('That position is not free, choose another one')
    
    #return position

def replay():
    play_again = input('Play again (Yes or No)? ')
    
    if play_again == 'Yes':
        return True 
    else:
        return False


##########################################################
# TO DO: use of main() to run game from terminal

print('Welcome to Tic Tac Toe!')
while True:
    # Set the game up here
    print('Initial Board is empty...')
    board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    #display_board(board)
    
    player_1_mark, player_2_mark = player_input() # tuple unpack X and O for each player
    print('Player 1 is ', player_1_mark)
    print('Player 2 is ', player_2_mark)
    
    next_to_go = choose_first() #'Player 1' or 'Player 2' randomly --> Alternating variable
    print(next_to_go + ' goes first')
    
    while not full_board_check(board): #while True, will break when board is full
        
        # Player 1 Turn 
        if next_to_go == 'Player 1':
            player_position = player_choice(board, next_to_go) # Select position in the board
            place_marker(board, player_1_mark, player_position) # place marker
            display_board(board) # display updated board
                        
            if win_check(board, player_1_mark): # returns True if there is a win
                print(next_to_go + ' has won the game')
                break
            
            next_to_go = 'Player 2' # switch player
        
        # Player 2 Turn
        if next_to_go == 'Player 2':
            player_position = player_choice(board, next_to_go) # Select position in the board
            place_marker(board, player_2_mark, player_position) # place marker
            display_board(board) # display updated board
            
            if win_check(board, player_2_mark): # returns True if there is a win
                print(next_to_go + ' has won the game')
                break
            
            next_to_go = 'Player 1' # switch player

    if not replay():
        break