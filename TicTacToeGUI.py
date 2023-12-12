# -*- coding: utf-8 -*-
"""
Created on Wed Dec 6 18:40 2023

@author: daveh


"""

import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        """
        Create instances of the game window, 
        board, player, and GUI buttons
        """
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.current_player = "X"
        self.board = [[" " for _ in range(3)] for _ in range (3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        
        
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(
                    self.window,
                    text = " ",
                    font = ("Segoe Script", 20),
                    width = 10,
                    height = 5,
                    command = lambda row = i, col = j: self.button_click(row,col)
                    )
                self.buttons[i][j].grid(row = i, column = j)
                
    def run(self):
        self.window.mainloop()
                
               
    def button_click(self, row, col):
        """
        The button click on screen is the event that will trigger
        all the functions to place token, check for win or draw, swap players,
        and reset the game

        """
            
        for r in self.board: print("before move: ", r)

        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            self.buttons[row][col]["text"] = self.current_player
            #print("After move: ", row)
            #self.change_player()
            #print(self.current_player())
        if self.is_winner():
            self.display_winner()
            self.game_reset()
        elif self.is_tie():
            self.display_tie()
            self.game_reset()
        else:
            self.change_player()
            
            
        for x in self.board: print("after move: ", x)
        
        print(self.current_player)
                    
        
    def is_winner(self):
    # CHECK ROWS
        for row in self.board:
           if row[0] == row[1] == row[2] != " ":
               return True
        
    # CHECK COLUMNS
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != " ":
                return True
            
    # CHECK DIAGONALS
        if(self.board[0][0] == self.board[1][1] == self.board[2][2] != " " or  
           self.board[0][2] == self.board[1][1] == self.board[2][0]):
        
             return True
               
        return False
   
    
    def is_tie(self):
        for row in self.board:
            if " " in row:
                return False
        return True
            
            
    def change_player(self):
        if self.current_player == "X":
            self.current_player = "O" 
        elif self.current_player == "O":
            self.current_player = "X"
        
    
               
               
    # DISLAY MESSAGES FOR A WIN OR TIED GAME
       
       
    def display_winner(self):
        messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} is the winner!")
           
           
    def display_tie(self):
        messagebox.showinfo("Tic Tac Toe", "The game is tied!")
           
       
           
       
    def game_reset(self):
        self.current_player = "X"
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons [i][j]["text"] = " "
        
    
        


if __name__ == "__main__":
    game = TicTacToe()
    game.run()

#game = TicTacToe()
#game.run()
