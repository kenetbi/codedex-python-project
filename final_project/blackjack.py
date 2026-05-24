import random, time
# Blackjack 

cards = ["ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king"] * 4
dealer_total = 0
player_total = 0
player_aces = 0
dealer_aces = 0
player_turn = True
dealer_turn = False
is_player_busted = False
is_dealer_busted = False

def is_busted(is_player_busted, is_dealer_busted):
    time.sleep(2)
    if is_player_busted:
        print("\nThe player BUSTED!")
        print("\nThe dealer WINS!!")
    elif is_dealer_busted:
        print("\nThe dealer BUSTED!")
        print("\nThe player WINS!!")

def is_winner(player_total, dealer_total):
    time.sleep(2)
    print(f"\nPlayer's total: {player_total}")
    print(f"Dealer's total: {dealer_total}")
    player_distance = 21 - player_total
    dealer_distance = 21 - dealer_total
    if player_distance < dealer_distance:
        print("\nThe player WINS!")
        print("Congratulations!")
    elif dealer_distance < player_distance:
        print("\nThe dealer WINS!")
        print("Better luck next time!")
    else:
        print("\n It's a TIE!")


dealer = random.sample(cards, 2)
player = random.sample(cards, 2)

for card in dealer:
    cards.remove(card)
    if isinstance(card, int):
        dealer_total += card
    elif card == "jack" or card == "queen" or card == "king":
        dealer_total += 10
    elif card == "ace":
        dealer_total += 11
        dealer_aces +=1

while dealer_total > 21 and dealer_aces > 0:
    dealer_total -= 10
    dealer_aces -= 1

for card in player:
    cards.remove(card)
    if isinstance(card, int):
        player_total += card
    elif card == "jack" or card == "queen" or card == "king":
        player_total += 10
    elif card == "ace":
        player_total += 11
        player_aces += 1

while player_total > 21 and player_aces > 0:
    player_total -= 10
    player_aces -= 1

print("=========================")
print("  Welcome to our Casino")
print("=========================")
print("")
print("Let us go play BlackJack!")
input("Press Enter to continue...")
print("")

print(f"Dealer's card: {dealer[0]} | Hidden")
print(f"Player's card: {player[0]} | {player[1]}")

is_player_blackjack = False
is_dealer_blackjack = False

if player_total == 21 and len(player) == 2:
    print("BLACKJACK!")
    is_player_blackjack = True
    dealer_turn = True

if not is_player_blackjack:
    while player_turn:
        if player_total > 21:
            print(f"Player's total: {player_total}")
            is_player_busted = True
            is_busted(is_player_busted, is_dealer_busted)
            break
        
        time.sleep(2)
        action = input("\nDo you 'hit' or 'stand'? ").lower().strip()
        print("")

        if action == "hit":
            player_hit = random.choice(cards)
            cards.remove(player_hit)
            player.append(player_hit)

            print("Player's card:", end=" | ")
            for x in player:
                print(f"{x}", end=" | ")
            print("")

            if isinstance(player_hit, int):
                player_total += player_hit
            elif player_hit in ["jack", "queen", "king"]:
                player_total += 10
            elif player_hit == "ace":
                player_total += 11
                player_aces += 1
                        
            while player_total > 21 and player_aces > 0:
                player_total -= 10
                player_aces -= 1  
        elif action == "stand":
            player_turn = False
            dealer_turn = True
        else:
            print("Invalid input, Try again!")
    
if not is_player_busted:
    print("\nThe dealer will now reveal his face-down card.")
    print(f"Dealer's card: {dealer[0]} | {dealer[1]}")
    if dealer_total == 21 and len(dealer) == 2:
                print("Dealer has BLACKJACK!")
                is_dealer_blackjack = True
    
    if not is_dealer_blackjack:
        while dealer_turn:
            time.sleep(2)
            if not is_player_blackjack:
                if dealer_total > 21:
                    print(f"Dealer total: {dealer_total}")
                    is_dealer_busted = True
                    is_busted(is_player_busted, is_dealer_busted)
                    break

                if dealer_total <= 16:
                    print("\nThe dealer will now draw a card.")
                    dealer_hit = random.choice(cards)
                    cards.remove(dealer_hit)
                    dealer.append(dealer_hit)

                    print("Dealer's card:", end=" | ")
                    for card in dealer:
                        print(f"{card}", end=" | ")
                    print("\n") 

                    if isinstance(dealer_hit, int):
                        dealer_total += dealer_hit
                    elif dealer_hit in ["jack", "queen", "king"]:
                        dealer_total += 10
                    elif dealer_hit == "ace":
                        dealer_total += 11
                        dealer_aces += 1

                    while dealer_total > 21 and dealer_aces > 0:
                        dealer_total -= 10
                        dealer_aces -= 1
                else:
                    print(f"The Dealer's total: {dealer_total}.")
                    print("The dealer stands.")
                    break
            else:
                break

        if not is_dealer_busted and not is_player_blackjack:
            is_winner(player_total, dealer_total)

if is_player_blackjack and is_dealer_blackjack:
    print("Both has BLACKJACK!\nIt's a TIE!")
elif is_player_blackjack:
    print("\nPlayer WINS!")
elif is_dealer_blackjack:
    print("\nDealer WINS!")