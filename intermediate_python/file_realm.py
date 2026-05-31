# lines = ["This is a line.\n", "This is the next line.\n", 'Myline\n', 'your line\n', 'his line\n', 'her line\n']

# with open("example.txt", "w") as file:
#     file.writelines(lines)

# with open("example.txt", "r") as file:
#     line1 = file.readlines()
#     for line in line1:
#         print(line, end="")

liked_songs = {
    "Pahina":"Cup of Joe",
    "Misteryoso": "Cup of Joe",
    "Raining In Manila": "Lola Amour",
    "Pasilyo": "SunKissed Lola",
    "Ere": "Juan Karlos",
    "Leave The Door Open": "Silk Sonic",
    "Die With A Smile": "Bruno Mars & Lady Gaga"}

def write_liked_songs_to_file(liked_songs, file_name):
    with open(file_name, "w") as file:
        file.write("Liked Songs:\n")
        for song, artist in liked_songs.items():
            file.write(f"{song} by {artist}\n")
    print(f"Liked! Successfully added to your list!")

write_liked_songs_to_file(liked_songs, "liked_songs.txt")