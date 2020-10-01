from typing import List


def swap(words: List[str], a: int, b: int):
    temp = words[a]
    words[a] = words[b]
    words[b] = temp


def reverse(words: List[str]):
    for i in range(len(words) // 2):
        swap(words, i, len(words) - 1 - i)


# Testing data below

people = [
    "Roy",
    "Maurice",
    "Jen",
    "Douglas",
    "Denholm",
    "Richmond"
]

reverse(people)
assert people == ["Richmond", "Denholm", "Douglas", "Jen", "Maurice", "Roy"]

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

reverse(fruits)
assert fruits == ["Honeysuckle", "Grape", "Feijoa", "Eucalyptus", "Durian", "Cherry", "Banana", "Apple"]

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

reverse(lyrics)
assert lyrics == ["you", "desert", "and", "around", "run", "gonna", "never", "down", "you",
                  "let", "gonna", "never", "up", "you", "give", "gonna", "never"]
print("Passed")
