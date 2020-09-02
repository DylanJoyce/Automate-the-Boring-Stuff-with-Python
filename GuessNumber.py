#!/usr/bin/env python

#Guess a Number
import random

secretNumber = random.randint(1,10)

print("I am thinking of a number between 1 and 20.")

guess = "a"

for numberOfGuessesTaken in range(1,6):
	print("Take a guess.")
	guess = int(raw_input())

	if guess < secretNumber:
		print("That guess is too low.")
	elif guess > secretNumber:
		print("That guess is too high.")
	
	if guess == secretNumber:
		break

if guess == secretNumber:
	print("Yes, the number was %i. You got it in %i guesses. Good job." %(secretNumber, numberOfGuessesTaken))
else:
	print("No, the number was %i. You exhausted you %i guesses." %(secretNumber, numberOfGuessesTaken))