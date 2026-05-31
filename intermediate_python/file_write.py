with open("diaries.txt",  "w") as file:
    file.write("LEARNING LIITLE BY LITTLE! SOON TO BE!\n")
    file.write("LEARNING LIITLE BY LITTLE! SOON TO BE!\n")
    file.write("LEARNING LIITLE BY LITTLE! SOON TO BE!\n") 

with open("diaries.txt", "a") as file:
    file.write("kenneth kenneht kenneth")

with open("diaries.txt", "r") as file:
    content = file.read()
    print(content)