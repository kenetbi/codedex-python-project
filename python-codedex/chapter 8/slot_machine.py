import random

symbols = ['🍒',' 🍇', '🍉', '7️⃣']
is_playing = True

def play():
  results = random.choices(symbols, k=3)
  print(f"{results[0]} | {results[1]} | {results[2]}")

  if results[0] == '7️⃣' and results[1] == '7️⃣' and results[2] == '7️⃣':
    print("JACKPOT!")
  else:
    print("Try Again")
  print("")

while is_playing:
  choice = input("Do you want to play?(Y/N) ").upper()
  if choice == "Y":
    play()
  elif choice == "N":
    print("Exiting the game...")
    is_playing = False
  else:
    print("Wrong input. Type Y for yes and N for no")
    continue