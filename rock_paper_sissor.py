import random

user_input = 0
computer_picks = 0

options = ['rock','paper','sissor']

while True:
    user_input = input("Type rock/paper/sissor or 'Q' to Quit ").lower()
    if user_input == 'Q':
        break
    if user_input not in options:
        continue

    random_number = random.randint(0,2)
    # rock = 0,paper = 1,sissor = 2 
    computer_picks = options[random_number]  
    print("computer picks : ",computer_picks,".") 

    if user_input == "rock" and computer_picks == "sissor":
        print("You won!!")
        user_input += 1

    elif user_input == "sissor" and computer_picks == "paper":
        print("You won!!")
        user_input += 1    

    elif user_input == "paper" and computer_picks == "rock":
        print("You won!!")
        user_input += 1   

    else:
        print("computer won , you lost :(")    
        computer_picks += 1


print("You won ",user_input,"times.")
print("Computer won ",computer_picks,"times.")
print("GoodBye")

