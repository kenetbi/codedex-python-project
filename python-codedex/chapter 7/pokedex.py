class Pokemon:
  def __init__(self, entry, name, types, description, is_caught):
    self.entry = entry
    self.name = name
    self.types = types
    self.description = description
    self.is_caught = is_caught

  def speak(self):
    print(f"{self.name} {self.name}")

  def display_details(self):
    print(f"Entry Number: {self.entry}")
    print(f"Name: {self.name}")
    print(f"Type: {self.types}")
    print(f"Description: {self.description}")
    if self.is_caught:
      print("Pikachu has already been caught!")
    else:
      print("Not yet caught!")

pikachu = Pokemon(25, "Pikachu", "Electric", "It has small electric sacs on both its cheeks. If threatened, it looses electric charges from the sacs.", True)
pikachu.speak()
pikachu.display_details()