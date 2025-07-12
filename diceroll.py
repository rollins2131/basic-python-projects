#loop
#ask roll the dice
#if user enters y then 
#genreate two random numbers
#print thm
#if user enters n then
# display thank u message and Terminate
#else 
#print invalid choice
import random
roll_count = 0

while True: # infinite loop
    choice = input("Roll the dice ? (y/n): ").lower()#whtever the user types we convert it to lower case
    if choice == 'y':
        try: 
            num_dice = int(input("How many dice u want to roll? "))
            if num_dice <=0:
                print("please enter a number greater than 0")
                continue
            
            dice = []
            for i in range(num_dice):
                dice.append(random.randint(1,6))
            print("you rolled",dice)
            roll_count+=1
            
        except ValueError:
            print("please enter a valid number")
      

    elif choice == 'n':
        print(f"Thanks for playing! You have rolled the dice {roll_count}times")
        break #come out the loop

    else: 
        print("Invalid choice !")


