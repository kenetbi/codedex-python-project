import random, inputimeout, time

def scene1(satisfaction):
    print(f"\nCURRENT SATISFACTION: {satisfaction}")
    print("SCENE 1: THE COUNTER")
    print("Choose your answer:")
    print("A customer is waiting for their food, but the floor is a slippery hazard from the spilled milk.")
    print("Choose your answer:")
    print("""A) Clean it yourself.
B) Put up a "Wet Floor" sign and keep taking orders.
C) Call a co-worker to clean it.""")
    
    valid_choice = True
    while valid_choice:
        choice = input("Enter your choice (A, B, or C): ").upper()
        print("")
        if choice == "A":
            print("Guarantees safety, but customers wait longer. Satisfaction -15")
            satisfaction -= 15
            valid_choice = False
        elif choice == "B":
            print("Fast! But a random check determines if a customer slips")
            satisfaction += 10
            is_slipped = random.choice([True, False])
            print("")
            time.sleep(2)
            if is_slipped:
                print("A customer slips! Satisfaction -15")
                satisfaction -= 25
            else:
                print("No one slips. Satisfaction +10")
                satisfaction += 20
            valid_choice = False
        elif choice == "C":
            print("Your co-worker cleans it immediately to prevent accidents. Satisfaction +20")
            satisfaction += 20
            valid_choice = False
        else:
            print("Invalid choice. Please enter A, B, or C.") 
    
    if satisfaction <= 0:
        return game_over(satisfaction)
    else:    
        return scene2(satisfaction)

def scene2(satisfaction):
    print(f"\nCURRENT SATISFACTION: {satisfaction}")
    print("SCENE 2: The Kitchen")
    print("The kitchen printer stops working. The cooks aren't receiving any order tickets, and orders are piling up!")
    print("Choose your answer:")
    print("""A) Scream the orders out loud.
B) Restart the printer.
C) Handwrite the tickets.""")
    
    has_receipt = True
    valid_choice = True
    while valid_choice:
        choice = input("Enter your choice (A, B, or C): ").upper()
        print("")
        if choice == "A":
           print("Saves time, but you might lose your voice or make a mistake. Satisfaction -10")
           satisfaction -= 10
           is_mistake = random.choice([True, False])
           has_receipt = False
           print("")
           time.sleep(2)
           if is_mistake:
               print("The customers are mad because their orders are different. Satisfaction -25")
               satisfaction -= 25
           else:
               print("The customers are leaving because of the screaming. - 20 Satisfaction")
               satisfaction -= 20
           valid_choice = False
        elif choice == "B":
            print("Takes a moment, but fixes the issue permanently. Satisfaction + 20")
            satisfaction += 20
            has_receipt = True
            valid_choice = False
            fast_fixed = random.choice([True, False])
            print("")
            time.sleep(2)
            if fast_fixed:
                print("The printer is fixed fast and the operation starts right away. Satisfaction + 15")
                satisfaction += 15
            else:
                print("The fix is taking time. Satisfaction - 10")
                satisfaction -= 10
            valid_choice = False
        elif choice == "C":
            print("Slow but accurate and the customer's are waiting patiently. Satisfaction + 15")
            satisfaction += 15
            has_receipt = True
            valid_choice = False
        else:
            print("Invalid choice. Please enter A, B, or C.") 

    if satisfaction <= 0:
        return game_over(satisfaction)
    else:   
        return scene3(satisfaction, has_receipt)

def scene3(satisfaction, has_receipt):
    print(f"\nCURRENT SATISFACTION: {satisfaction}")
    print("SCENE 3: The Drive-Thru")
    print("An angry customer at the Drive-Thru window says they’ve been waiting too long.")

    try:
        action = inputimeout.inputimeout(prompt = "Type 'APOLOGIZE': ", timeout = 5)
        print("")
        if action.upper() == "APOLOGIZE":
            print("The customer accepts the apologies and calmed down. Satisfaction + 1")
            satisfaction += 1
        else:
            print("Wrong word! They shout at you and threw their drink at the window. Satisfaction - 25")
            satisfaction -= 25
    except inputimeout.TimeoutOccurred:
        print("Too Slow! They drove off and leave a bad review for the bad service. Satisfaction - 20")
        satisfaction -= 20

    if satisfaction <= 0:
        return game_over(satisfaction)
    else:
        return scene4(satisfaction, has_receipt)

def scene4(satisfaction, has_receipt):
    print(f"\nCURRENT SATISFACTION: {satisfaction}")
    print("SCENE 4: The Storage Room")
    print("You completely ran out of the restaurant's signature sauce, and the lunch rush is at its peak.")
    print("You sprint to the dark back storage room to find the last box.")
    print("Choose your answer:")
    print("""A) Grab the heavy box on the top shelf.
B) Check the delivery area outside.
C) Use a substitute sauce.""")
    
    valid_choice = True
    while valid_choice:
        choice = input("Enter your choice (A, B, or C): ").upper()
        print("")
        if choice == "A":
           print("It has the risk of dropping it.")
           is_dropped = random.choice([True, False])
           print("")
           time.sleep(2)
           if is_dropped:
               print("You dropped it and there are no more sauces to use. Satisfaction -20")
               satisfaction -= 20
           else:
               print("You safely got the box. Satisfaction +25")
               satisfaction += 25
           valid_choice = False
        elif choice == "B":
            print("Takes longer, but it's safer. Satisfaction + 10")
            satisfaction += 10
            valid_choice = False
        elif choice == "C":
            print("Risky! Customers might notice.")
            is_noticed = random.choice([True, False])
            print("")
            time.sleep(2)
            if is_noticed:
                print("The customers noticed the change of sauce in taste. Satisfaction - 15")
                satisfaction -= 15
            else:
                print("The customers didn't notice the change of sauce. Satisfaction + 10")
                satisfaction += 10
            valid_choice = False
        else:
            print("Invalid choice. Please enter A, B, or C.") 

    if satisfaction <= 0:
        return game_over(satisfaction)
    else:   
        return scene5(satisfaction, has_receipt)

def scene5(satisfaction, has_receipt):
    print(f"\nCURRENT SATISFACTION: {satisfaction}")
    print("SCENE 5: The Register(BOSS FIGHT)")
    print("A customer comes up claiming they were overcharged by $50, and they are demanding to see the owner.")
    print("Choose your answer:")
    print("A) Find your customer's receipt copy. \nB) Call the Owner.")
    
    valid_choice = True
    while valid_choice:
        choice = input("Enter your choice (A or B): ").upper()
        print("")
        if choice == "A":
            if has_receipt:
               print("You saw the copy of the receipt and saw that there are no overcharged that happened.")
               print("The Owner comes and explain it clearly to the Customer.")
               print("Satisfaction +50")
               satisfaction += 50
            else:
               print("You don't have the receipt due to not working receipt printer.")
               print("The Owner takes over and refunded the money.")
               print("The owner scolds you and fired you off on the spot...")
               print("Satisfaction -50")
               satisfaction -= 50
            valid_choice = False
        elif choice == "B":
            if has_receipt:
                print("You immediately called the Owner.")
                print("The owner is looking for the receipts...")
                time.sleep(2)
                print("There is proof in the receipt, the Owner fights back and make the customer leave.")
                print("Satisfaction +50")
                satisfaction += 50
            else:
                print("The owner is mad because there are no available receipts.")
                print("The owner scolds you and fired you off on the spot...")
                print("To calm the customer, the owner refunded the money")
                print("Satisfaction -50")
                satisfaction -= 50
            valid_choice = False
        else:
            print("Invalid choice. Please enter A or B.") 

    if satisfaction <= 0:
        return game_over(satisfaction)
    else:   
        return winner(satisfaction)

def game_over(satisfaction):
    print(f"CURRENT SATISFACTION: {satisfaction}")
    print(f"Your satisfaction now reaches {satisfaction}, you didn't maintain the customer's satisfaction.")
    print("\nGAME OVER")

def winner(satisfaction):
    print(f"\nCURRENT SATISFACTION: {satisfaction}")
    print("You maintained the Customer's Satisfaction, you are a GOOD Employee!")
    print("\nCONGRATULATIONS!")



print("=================================================================")
print("                   WELCOME TO THE WEEKEND RUSH")
print("=================================================================")
print("""
It’s Sunday noon. The line of hungry customers is stretching out the front door,
the ticket printer is jamming, and your co-worker just accidentally spilled a 
giant jug of chocolate milk on the floor. You have to survive the shift!
""")

print("You have a Customer Satisfaction of 100.")
print("Make the right choice and keep the it to the highest!")
print("")

time.sleep(2)
scene1(100)
