#Refacorting is changing the structure of the code withtout changing its funcationality
# Now we refactor the code of rock paper and scisoors
import random 

Rock = 'r'
Scissor = 's'
paper = 'p'
emojis = { Rock:'rock',Scissor:'scissor',paper:'paper'}
choices = tuple(emojis.keys())

def get_user_choice():
    while True:
        user_choice = input("enter your choice (r/p/s)").lower()
        if user_choice in choices:
            return user_choice
        else: 
            print("Invalid choice")

def display_chocies(user_choice,computer_choice):
    print(f"Your choice {emojis[user_choice]}")
    print(f"computer choice {emojis[computer_choice]}")
    

def determine_winner(user_choice,computer_choice):
    if user_choice == computer_choice:
        print("Tie!")
    elif ( # by adding this () parthenthisis we can write multiple lines of code together without the problem of intendenation
        (user_choice == Rock and computer_choice == Scissor) or
        (user_choice == Scissor and computer_choice == paper) or
        (user_choice == paper and computer_choice == Rock)):
        print('You win')
    else:
        print("Computer win")


def play_game():

    while True:
        user_choice = get_user_choice()

        computer_choice = random.choice(choices)

        display_chocies(user_choice,computer_choice)

        determine_winner(user_choice,computer_choice)

        should_continue = input('continue? (y/n):').lower()
        if should_continue == 'n':
            print("Thank you for playing")
            break

play_game()
    




