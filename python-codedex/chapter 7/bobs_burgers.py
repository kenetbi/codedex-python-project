class Restaurant:
  name = ""
  restaurant_type = ""
  rating = 0
  is_open = False

bobs_burgers = Restaurant()

bobs_burgers.name = "Bob\'s Burgers"
bobs_burgers.restaurant_type = "American Diner"
bobs_burgers.rating = 4.7
is_open = True

print(vars(bobs_burgers))