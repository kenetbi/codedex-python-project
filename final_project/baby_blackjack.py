import random, time

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king"] * 4
dealer_total = 0
player_total = 0
player_turn = True
dealer_turn = True
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

for card in player:
    cards.remove(card)
    if isinstance(card, int):
        player_total += card
    elif card == "jack" or card == "queen" or card == "king":
        player_total += 10

print(f"Dealer's card: {dealer[0]} | Hidden")
print(f"Player's card: {player[0]} | {player[1]}")
print(f"Player's Total: {player_total}")

while player_turn:
    if player_total > 21:
        print(f"Player's total: {player_total}")
        is_player_busted = True
        is_busted(is_player_busted, is_dealer_busted)
        break
    time.sleep(2)
    action = input("\nDo you 'hit' or 'stand'? ").lower().strip()

    if action == "hit":
        player_hit = random.choice(cards)
        print(f"You draw: {player_hit}")
        cards.remove(player_hit)
        player.append(player_hit)

        print(f"Player's card:", end=" | ")
        for card in player:
            print(f"{card}", end=" | ")
        print("")

        if isinstance(player_hit, int):
            player_total += player_hit
        elif player_hit == "jack" or player_hit == "queen" or player_hit == "king":
            player_total += 10
    elif action == "stand":
        player_turn = False
    else:
        print("Invalid Input!")

if not is_player_busted:
    print("\nThe dealer will now reveal his face-down card.")
    while dealer_turn:
        print("Dealer's card:", end=" | ")
        for card in dealer:
            print(f"{card}", end=" | ")
        print("")

        time.sleep(2)
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

            if isinstance(dealer_hit, int):
                dealer_total += dealer_hit
            elif dealer_hit == "jack" or dealer_hit == "queen" or dealer_hit == "king":
                dealer_total += 10
        else:
            print(f"The Dealer's total: {dealer_total}.")
            print("The dealer stands.")
            break

    if not is_dealer_busted:
        is_winner(player_total, dealer_total)