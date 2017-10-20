'''This is a multiline comment
and will serve to describe rock-paper-scissors'''

from random import randint
from time import sleep

options = ["R", "P", "S"]

you_lose = "You lost!"
you_win = "You win!"

def decide_winner(user_choice, computer_choice):
  print "The user's choice is: %s" % user_choice
  print "Computer selecting..."
  sleep(1)
  print "The computer's choice is: %s" % computer_choice
  user_choice_index = options.index(user_choice)
  computer_choice_index = options.index(computer_choice)
  if user_choice_index == computer_choice_index:
    print "It's a tie!"
  elif user_choice_index == 0 and computer_choice_index == 2:
    print you_win
  elif user_choice_index == 1 and computer_choice_index == 0:
    print you_win
  elif user_choice_index == 2 and computer_choice_index == 1:
    print you_win
  elif user_choice_index > 2:
    print "Invalid option!"
  else:
 		print you_lose
  return


def play_RPS():
  print "Rock, Paper, Scissors?"
  sleep(1)
  user_choice = raw_input("Select R for Rock, P for Paper, or S for Scissors: ")
  user_choice = user_choice.upper()
  computer_choice = options[randint(0,len(options)-1)]
  decide_winner(user_choice, computer_choice)

play_RPS()