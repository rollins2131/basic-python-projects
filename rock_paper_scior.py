#Ask the user to make a Choice
#if choice is not valid
#print an error
#let the computer to make a choice
#print choices(emojis) 
#Determine the winner
# ASK the user if they want to continue
# if not 
# terminate
import random
emojs = {'r':'rock','s':'scissors','p':'paper'} 
choices = ('r','p','s')
while True:
    user_choice = input("Rock,paper,or scissors? (r/p/s): ").lower() # whether user type capital Y and N or small y and n it will be converted to small alphabets itself by using lower function
    if user_choice not in choices: # checks tht the choices made by user is in the choices tuple if not its invalid statement bro
        print("Invalid choice !")
        continue

    computer_choice = random.choice(choices)

    print(f"you choice {emojs[user_choice]}")#we are passing varibale user_choice inside the emojies dictionary if user selcets r it returns the rock becaz r is key and rock is value
    print(f"computer choice is {emojs[computer_choice]}")##we are passing varibale computeer_choice inside the emojies dictionary if computer seclects r it returns the rock becaz r is key and rock is value

    if user_choice == computer_choice:
        print("Tie!")
    elif ( # by adding this () parthenthisis we can write multiple lines of code together without the problem of intendenation
        (user_choice == 'r' and computer_choice == 's') or
        (user_choice == 's' and computer_choice == 'p') or
        (user_choice == 'p' and computer_choice == 'r')):
        print('You win')
    else:
        print("Computer win")

    should_contine = input ("continue ? (y/n): ").lower()
    if should_contine == 'n':
        print("Thank u for playing !")
        break
        



