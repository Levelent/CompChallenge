import re

with open("words.txt") as file:
    data = file.read()

corrupted = re.sub(r"[^\w]", "", data.lower())

with open("corrupted.txt", "w") as file:
    file.write(corrupted)
