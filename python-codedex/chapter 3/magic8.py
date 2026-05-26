import random

question = input("Question: ")

choices = ["Yes - definitely.",
          "It is decidedly so.",
          "Without a doubt.",
          "Reply hazy, try again.",
          "Ask again later.",
          "Better not tell you now.",
          "My sources say no.",
          "Outlook not so good.",
          "Very doubtful."]


answer = random.choice(choices)
print(answer)
