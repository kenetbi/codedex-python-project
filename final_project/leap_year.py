print("===============================")
print("Welcome to Leap year Calculator")
print("===============================")
print("")

while True:
    year = int(input("Input a year: "))

    if year % 400 == 0:
        print("Leap Year")
    elif year % 100 == 0:
        print("It is a common year")
    elif year % 4 == 0:
        print("Leap Year")
    else:
        print("It is a common year") 