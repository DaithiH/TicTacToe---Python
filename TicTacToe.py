# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 13:43:32 2023

@author: daveh
"""

"""
Second Attempt 
"""




def game_board():
    row1 = "{}|{}|{}".format(board[0], board[1], board[2])
    row2 = "{}|{}|{}".format(board[3], board[4], board[5])
    row3 = "{}|{}|{}".format(board[6], board[7], board[8])

    border = "-+-+-"
    
    print()
    print(row1)
    print(border)
    print(row2)
    print(border)
    print(row3)
    
def player_turn(token):
    """
    Function to allocate player tokens and check for 
    valid inputs. Checks space on the board and if empty places token.
    If space is full player is promped again.
    """
    
    if token == 'X':
        player = 1 
    elif token == 'O':
        player = 2
    
    print(f"Your move player {player}")
    
   
   
    while True:
        
        try:
            # TO HANDLE EXCEPTIONS LIKE INVALID NUMBER 
            # OR IF PLAYER INPUTS A NON-NUMERIC VALUE
            # WILL CATCH THE INVALID INPUT AND PROMPT
            # THE PLAYER AGAIN 
            move = int(input("Place your token (1-9): ").strip())
            # .strip() WILL REMOVE ANY WHITESPACE
            if 1 <= move <=9:
    
                if board[move-1] == " ":
                    board[move-1] = token
                    break
    
                else:
                    print("That square is full! Try again.")
                   # print("You must enter a number between 1-9. Try again.")
                   #move = int(input("Place your token (1-9): ").strip())

                
        except ValueError:
            print("You must enter a number between 1-9. Try again.")

                
            
            
def is_winner(token):
    """
    Checking board for winning combinations
    """
    if (board[0] == token and board[1] == token and board[2] == token) or \
       (board[3] == token and board[4] == token and board[5] == token) or \
       (board[6] == token and board[7] == token and board[8] == token) or \
       (board[0] == token and board[3] == token and board[6] == token) or \
       (board[1] == token and board[4] == token and board[7] == token) or \
       (board[2] == token and board[5] == token and board[8] == token) or \
       (board[0] == token and board[4] == token and board[8] == token) or \
       (board[2] == token and board[4] == token and board[6] == token):
           return True
    else:
        return False
    
def a_tie():
    if " " not in board:
        return True
    else:
        return False

def reset_board():
    global board
    board = [" " for x in range(9)]

def play_again():
    return input("Do you want to play again (y/n)?:").lower().startswith('y')
    

print("Welcome to my TicTacToe game!\n"
      "Take your move by entering the number of the square where you "
      "want to place your token.\n"
      "The board is indexed as follows:\n"
      " 1 | 2 | 3\n"
      " 4 | 5 | 6\n"
      " 7 | 8 | 9")    
                  
while True:
    board = [" " for x in range(9)]
    while True:
        game_board()
        player_turn('X')
    
        if is_winner("X"):
            print("Player 1 wins!")
            break
        elif a_tie():
            print("The game is tied!")
            break
        
        game_board()
    
        player_turn('O')
    
    
        if is_winner("O"):
            print("Player 2 wins!")
            break
        elif a_tie():
            print("The game is tied!")
            break
    
    if not play_again():
        print('Thank you for playing!')
        break
    else:
        reset_board()
        
    
    
  
    
    
        
        
    
    
    
    
    
        



