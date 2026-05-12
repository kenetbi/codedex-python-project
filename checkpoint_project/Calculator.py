import math

is_running = True

print("""
==================
Area Calculator 📐
==================""")

while is_running:

    print("""
1) Triangle
2) Rectangle
3) Square
4) Circle
5) Quit
      """)
    
    shape = int(input("Choose a shape (1-5): "))
    print("")
    if shape == 1:
        base = float(input("Base: "))
        height = float(input("Height: "))
        area = (height * base) / 2
        print("")
        print(f"The area is {area:.0f}")
    elif shape == 2:
        length = float(input("Length: "))
        width = float(input("Width: "))
        area = length * width
        print("")
        print(f"The area is {area:.0f}")
    elif shape == 3:
        side = float(input("Side: "))
        area = side ** 2
        print("")
        print(f"The area is {area:.0f}")
    elif shape == 4:
        radius = float(input("Radius: "))
        area = math.pi * (radius ** 2)
        print("")
        print(f"The area is {area:.0f}")
    elif shape == 5:
        print("Exiting the program.")
        is_running = False
    else:
        print("Invalid Input.")
