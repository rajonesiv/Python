#Author: Andrew Jones
#Python program for Battleship!
#Taken after the Battleship tutorial on Codecademy

#import the library for the random integers
from random import randint

#Define the board space, 10 x 10, and print it out
board = []

for i in range(10):
	board.append(['O'] * 10)

def print_board(board):
	for row in board:
		print " ".join(row)
	
print_board(board)
# 