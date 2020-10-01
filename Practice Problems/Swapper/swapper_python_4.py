from typing import List


def swap(words: List[str], a: int, b: int):
    temp = words[a]
    words[a] = words[b]
    words[b] = temp


def sort(words: List[str]):
    for i in range(len(words) - 1):
        swapped = False

        for j in range(len(words) - 1 - i):
            if words[j + 1] < words[j]:
                swap(words, j, j + 1)
                swapped = True

        if not swapped:
            break


# Testing data below

people = [
    "Roy",
    "Maurice",
    "Jen",
    "Douglas",
    "Denholm",
    "Richmond"
]

sort(people)
assert people == ["Denholm", "Douglas", "Jen", "Maurice", "Richmond", "Roy"]

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

sort(fruits)
assert fruits == ["Apple", "Banana", "Cherry", "Durian", "Eucalyptus", "Feijoa", "Grape", "Honeysuckle"]

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

sort(lyrics)
assert lyrics == ["and", "around", "desert", "down", "give", "gonna", "gonna", "gonna",
                  "let", "never", "never", "never", "run", "up", "you", "you", "you"]
print("Passed")
