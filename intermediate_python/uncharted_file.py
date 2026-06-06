secret_message = "This is a Secret Message!"

with open("secret_message.txt", "w") as file:
    file.write(secret_message)

with open("secret_message.txt", "r+") as file:
    original_message = file.read()
    unsent_message = "This message has been unsent."
    
    file.seek(0)

    file.truncate(len(unsent_message))
    file.write(unsent_message)

print(original_message)
print(unsent_message)