import random

def fortune(number):
  if number == 1:
    print("Don't pursue happiness – create it.")
  elif number == 2:
    print("All things are difficult before they are easy.")
  elif number == 3:
    print("The early bird gets the worm, but the second mouse gets the cheese.")
  elif number == 4:
    print("Someone in your life needs a letter from you.")
  elif number == 5:
    print("Don't just think. Act!")
  elif number == 6:
    print("Your heart will skip a beat.")
  elif number == 7:
    print("The fortune you search for is in another cookie.")
  elif number == 8:
    print("Help! I'm being held prisoner in a Chinese bakery!")


cookie1 = random.randint(1, 8)
cookie2 = random.randint(1, 8)
cookie3 = random.randint(1, 8)

fortune(cookie1)
fortune(cookie2)
fortune(cookie3)