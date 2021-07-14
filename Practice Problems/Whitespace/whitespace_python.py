class Solution:
    def reconstruct(self, corrupt, words: list):
        res = list(self._search(corrupt, set(words)))  # Enter into recursive function
        return ["".join(r)[:-1] for r in res]  # Note: we need to chop of a space at the end

    def _search(self, corrupt, words: set):
        if len(corrupt) == 0:
            # The string has been completely matched.
            return [""]
        elif len(words) == 0:
            # There are no possible matches that can be made.
            return []

        new_suffixes = []
        for i in range(len(corrupt)):
            section = corrupt[:i+1]
            if section in words:
                # Find all possible suffixes of the remaining string spacing.
                less_words = words.copy()
                less_words.remove(section)
                suffixes = self._search(corrupt[i+1:], less_words)
                # Add these longer suffixes to be passed up.
                new_suffixes.extend([f"{section} {suffix}" for suffix in suffixes])
        return new_suffixes


s = Solution()
print(s.reconstruct("eyestick", ["eye", "eyes", "tick", "stick", "yes"]))
print(s.reconstruct("baba", ["b", "a", "ba"]))
print(s.reconstruct("grandmashredderail", ["ail", "and", "derail", "era", "grand", "grandma", "mash", "rail", "red", "redder", "shred", "shredder"]))
print(s.reconstruct("eyestick", ["eye", "eyes", "tick", "stick", "yes", "e"]))
print(s.reconstruct("aab", ["a", "aa", "ab"]))
print(s.reconstruct("cdd", ["c", "cd", "d"]))
print(s.reconstruct("ffff", ["ff", "f", "fff"]))
print(s.reconstruct("low", ["lower", "wol", "er", "w"]))
print(s.reconstruct("hellothere", ["hello"]))
print(s.reconstruct("qwertyuiopasdfghjklzxcvbnm", ["qw", "q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m"]))
print(s.reconstruct("dabcbda", ["a", "b", "c", "d", "da", "bcb"]))
print(s.reconstruct("A1B2C3", ["1B", "3C", "2", "C3", "A", "A1"]))
print(s.reconstruct("aaaaaabbbbbbcccccc", ["a", "aa", "aaa", "aaaa", "aaaaa", "b", "bb", "bbb", "bbbb", "bbbbbb", "c", "cc", "ccc", "ccccc", "cccccc"]))
