# Sample Solution - There are some improvements that could still be made!
from typing import List, Set


def whitespace(corrupt: str, words: List[str]) -> List[str]:
    res = find_possible_spacings(corrupt, set(words))  # Recursive function entry point
    return ["".join(r) for r in res]


# Recursive function will do the bulk of the work
def find_possible_spacings(corrupt, words: Set[str]) -> List[str]:
    if len(corrupt) == 0:  # String completely matched.
        return [""]

    possible_spacings = []
    for i in range(len(corrupt)):
        # Take first i characters of string
        candidate = corrupt[:i+1]

        if candidate in words:
            # Add all possible spacings for the remaining string.
            remaining_words = words.copy()
            remaining_words.remove(candidate)
            suffixes = find_possible_spacings(corrupt[i+1:], remaining_words)

            for suffix in suffixes:
                if suffix == "":  # Don't add space if empty suffix
                    possible_spacings.append(candidate)
                else:
                    possible_spacings.append(f"{candidate} {suffix}")
    return possible_spacings


# Tests
if __name__ == "__main__":
    assert whitespace("hellothere", ["hello"]) == []
    assert whitespace("low", ["er", "lower", "w", "wol"]) == []
    assert whitespace("aab", ["a", "aa", "ab"]) == ["a ab"]
    assert whitespace("cdd", ["c", "cd", "d"]) == ["cd d"]
    assert whitespace("ffff", ["f", "ff", "fff"]) == ["f fff", "fff f"]
    assert whitespace("dabcbda", ["a", "b", "bcb", "c", "d", "da"]) == ["d a bcb da", "da bcb d a"]
    assert whitespace("eyestick", ["e", "eye", "eyes", "stick", "tick", "yes"]) == ["e yes tick", "eye stick", "eyes tick"]
    assert whitespace(
        "grandmashredderail",
        ["ail", "and", "ash", "derail", "era", "grand", "grandma", "mash", "rail", "ran", "red", "redder", "shred", "shredder"]
    ) == ["grand mash red derail", "grand mash redder ail", "grandma shred derail", "grandma shredder ail"]
    assert whitespace(
        "qwertyuiopasdfghjklzxcvbnm",
        ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "qw", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    ) == ["q w e r t y u i o p a s d f g h j k l z x c v b n m", "qw e r t y u i o p a s d f g h j k l z x c v b n m"]
