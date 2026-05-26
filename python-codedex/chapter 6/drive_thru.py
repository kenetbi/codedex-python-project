def welcome(name):
  print(f"Welcome to McDonald's {name}")
  print("Here is the Menu\n1 Cheeseburger\n2 Fries\n3 Soda\n4 Ice Cream\n5 Cookie")
  order = int(input("May I know your order please? "))
  return get_item(order)
  
def get_item(number):
  if number == 1:
    print("Cheeseburger")
  elif number == 2:
    print("Fries")
  elif number == 3:
    print("Soda")
  elif number == 4:
    print("Ice Cream")
  elif number == 5:
    print("Cookie")
  else:
    print("Order not on the Menu.")

name = input("Hello Mr?: ")
welcome(name)