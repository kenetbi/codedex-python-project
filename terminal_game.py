import time
# Day in my Life: Terminal Game
score = 0
is_running = True

while is_running:
    print("""
=============================================
Welcome to the Day in my Life: Terminal Game!""")
    print("1. Start Game")
    print("2. Exit")
    
    choice = int(input("Enter your choice: "))
    print("")
    
    if choice == 1:
        print("Starting the game...", end=" ")
        
    elif choice == 2:
        print("Exiting the game. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
        continue
    
    time.sleep(2)
    print("ENJOY!")
    print("\nYou are a young adult living in a bustling city. Your day starts at 7:00 AM. Let's see how your day unfolds!")

    is_awake = True
    while is_awake:
        print("\nIt is 6:00 AM. You wake up to the sound of your alarm.")
        print("What do you do?")
        print("1. Get out of bed and start your day.")
        print("2. Hit the snooze button and go back to sleep.")
        choice1 = int(input("Enter your choice(1 or 2): "))

        if choice1 == 1:
            print("\nYou get up, prepare and eat your breakfast, and got dressed for the work. ")
            score += 10
            is_awake = False
        elif choice1 == 2:
            print("\nYou slept again but rushed at preparing and getting to work.")
            print("Now you didn't get to eat breakfast. And head straight to work.")
            score -= 5
            is_awake = False
        else:
            print("\nInvalid choice. Please try again.")
            continue
    time.sleep(2)
    print("\nYou leave your house. On the way to work, you encounter a traffic jam." )
    if choice1 == 1:
        print("Since you woke up early, you have enough time to wait for the traffic to clear.")
        score += 5
        while True:
            print("\nYou arrive at work on time and got enough time.")
            time.sleep(1)
            print("What do you do?")
            print("1. Use the extra time to prepare for your meetings.")
            print("2. Use the extra time to relax and take a break.")
            choice2 = int(input("Enter your choice(1 or 2): "))

            if choice2 == 1:
                print("\nYou prepare for your meetings and impress your boss with your knowledge and confidence.")
                score += 10
                break
            elif choice2 == 2:
                print("\nYou take a break and relax, but you feel unprepared for your meetings.")
                score -= 5
                break
            else:
                print("\nInvalid choice. Please try again.")
                continue

    elif choice1 == 2:
        print("Since you woke up late, you are running late for work. You decide to take a detour through the city streets.")
        score -= 5
        while True:
            print("\nYou get lost in the city and end up being late for work.")
            time.sleep(1)
            print("What do you do?")
            print("1. Apologize to your boss and explain the situation.")
            print("2. Try to sneak into work without being noticed.")
            choice2 = int(input("Enter your choice(1 or 2): "))

            if choice2 == 1:
                print("\nYour boss appreciates your honesty and understanding, but you still get a warning for being late.")
                score += 10
                break
            elif choice2 == 2:
                print("\nYou get caught by your boss and face consequences for being late.")
                score -= 5
                break
            else:
                print("\nInvalid choice. Please try again.")
                continue

    time.sleep(2)
    while True:
        print("\nAfter a long day at work, you head back home. On the way, you encounter a street performer playing music.")
        print("What do you do?")
        print("1. Stop, give a tip and listen to the music.")
        print("2. Ignore the performer and continue walking.")
        choice3 = int(input("Enter your choice(1 or 2): "))

        if choice3 == 1:
            print("\nYou enjoyed the music and now you feel relaxed.")
            score += 10
            break
        elif choice3 == 2:
            print("\nYou ignore the performer and head straight home.")
            score += 10
            break
        else:
            print("\nInvalid choice. Please try again.")
            continue
    time.sleep(2)
    print("\nYou arrive home and reflect on your day.")
    if choice3 == 1:
        print("You are tired, and got home late at night.")
        while True:
            print("What do you do?")
            print("1. Play videogame until midnight.")
            print("2. Eat dinner and head straight to bed.")
            choice4 = int(input("Enter your choice(1 or 2): "))
            if choice4 == 1:
                print("\nYou had fun playing videogame, but you are exhausted the next day.")
                score -= 15
                break
            elif choice4 == 2:
                print("\nYou had a good night's sleep and feel refreshed the next day.")
                score += 10
                break
            else:
                print("\nInvalid choice. Please try again.")
                continue
    if choice3 == 2:
        print("You are tired, and got home early at night.")
        while True:
            print("What do you do?")
            print("1. Prepare dinner, eat, and study until bedtime.")
            print("2. Prepare dinner, eat, and play videogame until midnight.")
            choice4 = int(input("Enter your choice(1 or 2): "))
            if choice4 == 1:
                print("\nYou had a good night's sleep and learned a lot of things.")
                score += 10
                break
            elif choice4 == 2:
                print("\nYou had fun playing videogame, but you are exhausted the next day.")
                score += 10
                break
            else:
                print("\nInvalid choice. Please try again.")
                continue
    
    print(f"\nYour final score for the day is: {score}")
    if score >= 30:
        print("\nCongratulations! You had a great day and made the most out of it!")
    elif score < 30 and score >= 15:
        print("\nYou had a decent day and made some good choices.")
    elif score < 15 and score > 5:
        print("\nYou had a rough day, but there's always tomorrow.")
    else:
        print("\nYou had a terrible day. Better luck next time!")
