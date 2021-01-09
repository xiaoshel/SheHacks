person = input('Enter your name: ')
print("Hello "+ person + ". Welcome to the Number Guessing game!")

input_var = None

while type(input_var) is not int:
    input_var = input ("Please choose the lower end of your range of numbers: ")
    if input_var.isdigit():
        input_var=int(input_var)
    else:
        print("Input is not valid. Please enter an integer")

input_var2 = None

while type(input_var2) is not int:
	input_var2 = input("Now, please choose the higher end of your range of numbers: ")
	if input_var2.isdigit():
	    input_var2=int(input_var2)
	else:
	    print("Input is not valid. Please enter an integer")

print ("You set a range of", int(input_var), "and", int(input_var2))

import random
number= random.randrange(int(input_var), int(input_var2)) 



# program prompts user to guess random number
print ("I've picked a number from the range that you've chosen. Which number did I pick?")
        
guess = None

while type(guess) is not int:
    guess = input("My guess: ")
    if guess.isdigit():
        guess=int(guess)
        while type(guess) is int:
            guess = int(input("My guess: "))
            if (int(guess) < number): 
                print ("Incorrect. The number is higher")
            if (int(guess) > number): 
                print ("Incorrect. The number is lower")
            if (int(guess) == number): 
                print("Congratulations! You guessed the number")
    else:
        print("Error, only integers allowed. Please try again.")









