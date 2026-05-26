Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

print("Type the number of your answer.")

question1 = int(input("""
Q1) Do you like Dawn or Dusk?
    1) Dawn
    2) Dusk
Answer: """))
if question1 == 1:
  Gryffindor += 1
  Ravenclaw += 1
elif question1 == 2:
  Hufflepuff += 1
  Slytherin += 1
else:
  print("Wrong input.")

question2 = int(input("""
Q2) When I’m dead, I want people to remember me as:
    1) The Good
    2) The Great
    3) The Wise
    4) The Bold
Answer: """))
if question2 == 1:
  Hufflepuff += 2
elif question2 == 2:
  Slytherin += 2
elif question2 == 3:
  Ravenclaw += 2
elif question2 == 4:
  Gryffindor += 2
else:
  print("Wrong input.")

question3 = int(input("""
Q3) Which kind of instrument most pleases your ear?
    1) The violin
    2) The trumpet
    3) The piano
    4) The drum
Answer: """))
if question3 == 1:
  Slytherin += 4
elif question3 == 2:
  Hufflepuff += 4
elif question3 == 3:
  Ravenclaw += 4
elif question3 == 4:
  Gryffindor += 4
else:
  print("Wrong input.")

print()
print(f"Gryffindor: {Gryffindor}")
print(f"Ravenclaw: {Ravenclaw}")
print(f"Hufflepuff: {Hufflepuff}")
print(f"Slytherin: {Slytherin}")

house = max(Gryffindor, Ravenclaw, Hufflepuff, Slytherin)
print()

if Gryffindor > Ravenclaw and Gryffindor > Hufflepuff and Gryffindor > Slytherin:
  print("You are in the house of Gryffindor!")
elif Ravenclaw > Gryffindor and Ravenclaw > Hufflepuff and Ravenclaw > Slytherin:
  print("You are in the house of Ravenclaw!")
elif Hufflepuff > Gryffindor and Hufflepuff > Ravenclaw  and Hufflepuff > Slytherin:
  print("You are in the house of Hufflepuff!")
else:
  print("You are in the house of Slytherin!")