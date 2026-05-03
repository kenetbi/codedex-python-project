import random

is_running = True

print("""
================================
Rock Paper Scissors Lizard Spock
================================""")

while is_running:
    print("""
===================
1) ✊
2) ✋
3) ✌️
4) 🦎
5) 🖖 
6) Quit""")

    player = int(input("Choose your move (1-6): "))
    computer = random.randint(1, 5)
    print("")

    if player == 1 and computer == 1: # for tie condition
        print("You chose: ✊")
        print("Computer chose: ✊")
        print("It's a tie!")
    elif player == 1 and computer == 3:
        print("You chose: ✊")
        print("Computer chose: ✌️")
        print("You win!")
    elif player == 1 and computer == 4:
        print("You chose: ✊")
        print("Computer chose: 🦎")
        print("You Win!")
    elif player == 1 and computer == 5:
        print("You chose: ✊")
        print("Computer chose: 🖖")
        print("You lose!")
    elif player == 1 and computer == 2:
        print("You chose: ✊")
        print("Computer chose: ✋")
        print("You lose!")

    elif player == 2 and computer == 2: # for tie condition
        print("You chose: ✋")
        print("Computer chose: ✋")
        print("It's a tie!")
    elif player == 2 and computer == 1:
        print("You chose: ✋")
        print("Computer chose: ✊")
        print("You win!")
    elif player == 2 and computer == 5:
        print("You chose: ✋")
        print("Computer chose: 🖖")
        print("You win!")
    elif player == 2 and computer == 4:
        print("You chose: ✋")
        print("Computer chose: 🦎")
        print("You lose!")
    elif player == 2 and computer == 3:
        print("You chose: ✋")
        print("Computer chose: ✌️")
        print("You lose!")

    elif player == 3 and computer == 3: # for tie condition
        print("You chose: ✌️")
        print("Computer chose: ✌️")
        print("It's a tie!")    
    elif player == 3 and computer == 2:
        print("You chose: ✌️")
        print("Computer chose: ✋")
        print("You win!")
    elif player == 3 and computer == 4:
        print("You chose: ✌️")
        print("Computer chose: 🦎")
        print("You win!")
    elif player == 3 and computer == 5:
        print("You chose: ✌️")
        print("Computer chose: 🖖")
        print("You Lose!")
    elif player == 3 and computer == 1:
        print("You chose: ✌️")
        print("Computer chose: ✊")
        print("You lose!")
    
    elif player == 4 and computer == 4: # for tie condition
        print("You chose: 🦎")
        print("Computer chose: 🦎")
        print("It's a tie!")
    elif player == 4 and computer == 2:
        print("You chose: 🦎")
        print("Computer chose: ✋")
        print("You Win!")
    elif player == 4 and computer == 5:
        print("You chose: 🦎")
        print("Computer chose: 🖖")
        print("You win!")
    elif player == 4 and computer == 1:
        print("You chose: 🦎")
        print("Computer chose: ✊")
        print("You Lose!")
    elif player == 4 and computer == 3:
        print("You chose: 🦎")
        print("Computer chose: ✌️")
        print("You lose!")
    
    elif player == 5 and computer == 5: # for tie condition
        print("You chose: 🖖")
        print("Computer chose: 🖖")
        print("It's a tie!")
    elif player == 5 and computer == 1:
        print("You chose: 🖖")
        print("Computer chose: ✊")
        print("You Win!")
    elif player == 5 and computer == 3:
        print("You chose: 🖖")
        print("Computer chose: ✌️")
        print("You Win!")
    elif player == 5 and computer == 2:
        print("You chose: 🖖")
        print("Computer chose: ✋")
        print("You lose!")
    elif player == 5 and computer == 4:
        print("You chose: 🖖")
        print("Computer chose: 🦎")
        print("You lose!")
    

    elif player == 6:
        print("Exiting the program.")
        is_running = False
    else:
        print("Invalid Input.")
