import random,time

dice_numbers = range(1,7)
die_rolled = random.choices(dice_numbers, k=3)
total = 0

for die in die_rolled:
    total += die
print("Rolling the dice...")
time.sleep(2)
print(f"You rolled a {die_rolled[0]}, {die_rolled[1]}, and {die_rolled[2]}")
print(f"Your total score is {total}")
