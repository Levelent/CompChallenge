from typing import List


def swap(words: List[str], a: int, b: int):
    temp = words[a]
    words[a] = words[b]
    words[b] = temp


# Testing data below

people = [
    "Roy",
    "Maurice",
    "Jen",
    "Douglas",
    "Denholm",
    "Richmond"
]

swap(people, 0, 1)
swap(people, 0, 4)
swap(people, 1, 3)
assert people == ["Denholm", "Douglas", "Jen", "Roy", "Maurice", "Richmond"]

fruits = [
    "Apple",
    "Banana",
    "Cherry",
    "Durian",
    "Eucalyptus",
    "Feijoa",
    "Grape",
    "Honeysuckle"
]

swap(fruits, 3, 4)
swap(fruits, 5, 6)
swap(fruits, 5, 6)
swap(fruits, 2, 7)
assert fruits == ["Apple", "Banana", "Honeysuckle", "Eucalyptus", "Durian", "Feijoa", "Grape", "Cherry"]

lyrics = [
    "never",
    "gonna",
    "give",
    "you",
    "up",
    "never",
    "gonna",
    "let",
    "you",
    "down",
    "never",
    "gonna",
    "run",
    "around",
    "and",
    "desert",
    "you"
]

swap(lyrics, 0, 16)
swap(lyrics, 3, 4)
swap(lyrics, 4, 14)
swap(lyrics, 7, 12)
swap(lyrics, 14, 16)
assert lyrics == ["you", "gonna", "give", "up", "and", "never", "gonna", "run", "you",
                  "down", "never", "gonna", "let", "around", "never", "desert", "you"]
print("Passed")
