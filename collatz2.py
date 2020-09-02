#Write a function named collatz() that has one parameter named number. 
#If number is even, then collatz() should print number // 2 and return this value. 
#If number is odd, then collatz() should print and return 3 * number + 1.

def collatz(number):
	if number % 2 == 0:
		return 2
	elif:
		return 3 * number + 1

n = input('What is your number?')

collatz(n)