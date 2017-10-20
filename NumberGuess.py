"""
This program is designed to roll a pair of dice and have the user guess a number. The program shoud then determine a winner.
"""
from random import randint
from time import sleep

#prompt user for guess
def get_user_guess():
		user_guess = int(raw_input("Guess a number: "))
		return user_guess

#randomly roll a dice
def roll_dice(number_of_sides):
		first_roll = randint(1, number_of_sides)
		second_roll = randint(1, number_of_sides)
		max_val = number_of_sides * 2
		print "The maximum possible value is: " + str(max_val)
		sleep(1)
		user_guess = get_user_guess()   
#determine winner of the game
		if user_guess > max_val:
				print "Your guess is invalid! You can't guess higher than the maximum value!"
				return
		else:
				print "Rolling..."
				sleep(1)
				print "The first value is: %d" % first_roll
				sleep(1)
				print "The second value is: %d" % second_roll
				sleep(1)
				total_roll = first_roll + second_roll
				print "Result..."
				sleep(1)
				if user_guess > total_roll:
						print "Mission accomplished"
						return
				else:
						print "You've done your country a service."
						return
          
roll_dice(20)