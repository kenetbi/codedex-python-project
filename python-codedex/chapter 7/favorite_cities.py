class City:
  def __init__(self, name, country, population, landmarks, nickname, island, weather):
    self.name = name
    self.country = country
    self.population = population
    self.landmarks = landmarks
    self.nickname = nickname
    self.island = island
    self.weather = weather

bulacan = City("Bulacan", "Philippines", 500, ["Norzagaray", "DRT"], "Land of the heroes", False, "Summer")

print(vars(bulacan))