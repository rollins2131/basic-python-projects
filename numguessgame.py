#geneate a random number
#Loop
# Ask the user to make a guess
# if not a valid number
#print an error
#if number< guess
#print too low
#if number > guess
#print too high
#else
#print well done

import random
attempts = 0
number_to_guess = random.randint(1,100) #random function to generate number between 1 and 100 
while True: #infinate loop which breaks when you find the correct number 
    try: 
        guess= int(input(" guesss the num between 1 and 100: "))
        attempts+=1
        if guess < number_to_guess:
           print("Too low!")
        elif guess>number_to_guess:
           print("Too highh!")
        else:
           print(f"congratulations! you guessed the number., and you have attempted {attempts} times")
           break

    except ValueError:
        print("Please enter a valid number")





