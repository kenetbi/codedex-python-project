import random

open_again = True

def fortune_cookie():
    fortunes = ["A thrilling time is in your immediate future.",
               "Your hard work will soon pay off.",
               "A pleasant surprise is waiting for you.",
               "Your patience will be rewarded very soon.",
               "Adventure can be found around every corner.",
               "Your kindness is a gift to everyone you meet.",
               "A new perspective will bring you great clarity.",
               "Success is the result of your steady preparation.",
               "You are headed for a very important journey.",
               "Your creative energy will lead to a breakthrough."]
    fortune = random.choice(fortunes)
    return fortune

while open_again:
    crack_cookie = input("Do you want to open a Fortune Cookie?(Y/N) ").upper()

    if crack_cookie == "Y":
        input("Press Enter to Open your Fortune Cookie...")
        print(f"'{fortune_cookie()}'")
        print("")
    elif crack_cookie == "N":
        print("Exiting...")
        break
    else:
        print(crack_cookie, "is an invalid input.")
