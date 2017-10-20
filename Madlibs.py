"""
	This program prompts the user for input and prints the entire Mad Libs story with the user's input in the right places.
  Author: Andrew Jones
"""
print "Mad Libs is starting!"
name = raw_input("Please enter a name:  ")
snd_name = raw_input("Enter another name: ")
pl_pro = raw_input("Enter a plural pronoun")
adverb = raw_input("Enter an adverb: ")
first_adj = raw_input("Enter an adjective: ")
"""second_adj = raw_input("Enter a second adjective: ")
third_adj = raw_input("Enter one more adjective: ")"""
first_verb = raw_input("Enter a verb: ")
second_verb = raw_input("Enter a second verb: ")
"""third_verb = raw_input("Enter one more verb: ")"""
body = raw_input("Enter a part of the body: ")
first_noun = raw_input("Enter a noun: ")
"""second_noun = raw_input("Enter a second noun: ")
third_noun = raw_input("Enter a third noun: ")
fourth_noun = raw_input("Enter one more noun: ")
animal = raw_input("Enter an animal: ")
food = raw_input("Enter a food: ")
fruit = raw_input("Enter a fruit: ")"""
number = raw_input("Enter a number: ")
"""superhero = raw_input("Enter a superhero name: ")
country = raw_input("Enter a country: ")
dessert = raw_input("Enter a dessert: ")
year = raw_input("Enter a year: ")"""
#The template for the story
STORY = "Dear %s, You are extremly %s and I %s you! I want kiss your %s %s times. You make my %s burn with desire. When I first saw you, I %s stared at you and fell in love. Will you %s out with me? Don`t let your parents discourage you, %s are just jealous. Yours forever, %s"
print STORY % (name, first_adj, first_verb, body, number, first_noun, adverb, second_verb, pl_pro, name)
