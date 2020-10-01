from typing import List


def swap(words: List[str], a: int, b: int):
    temp = words[a]
    words[a] = words[b]
    words[b] = temp


def shift(words: List[str]):
    for i in range(len(words) - 1, 0, -1):
        swap(words, i - 1, i)


# Testing data below

people = [
    "Roy",
    "Maurice",
    "Jen",
    "Douglas",
    "Denholm",
    "Richmond"
]

shift(people)
assert people == ["Richmond", "Roy", "Maurice", "Jen", "Douglas", "Denholm"]

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

shift(fruits)
assert fruits == ["Honeysuckle", "Apple", "Banana", "Cherry", "Durian", "Eucalyptus", "Feijoa", "Grape"]

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

shift(lyrics)
assert lyrics == ["you", "never", "gonna", "give", "you", "up", "never", "gonna", "let",
                  "you", "down", "never", "gonna", "run", "around", "and", "desert"]
print("Passed")
