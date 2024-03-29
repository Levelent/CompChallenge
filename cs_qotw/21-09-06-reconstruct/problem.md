# Reconstruct

**Difficulty Range:** ⭐⭐⭐ - ⭐⭐⭐⭐
**Tags**: `recursion`, `backtracking`

*Thanks to a certain mishap involving someone being too trigger-happy with their regex substitutions, 
it looks like you're the one who has to fix the digitised texts of the national newspaper archives.*

We say a string is **corrupted** if it has been stripped of all whitespace and punctuation, then converted to lowercase.

## ⭐⭐⭐ Whitespace

To test a basic fix, you aim to create a function - it will take a non-empty **corrupted** string and a list of 
unique non-empty strings (our **words**), in order to **reconstruct** all possible spacings - but avoiding word reuse. 
For now, don't worry about capitalisation or punctuation.

### Inputs:
- A non-empty string no longer than 30 characters.
- A word list of at most 30 non-empty strings, in alphabetical order.
- Each element of the word list is no longer than 10 characters.

### Output:
- A list of all possible reconstructions of the corrupted string, in alphabetical order.
- If there are no reconstructions, return the empty list.

### Examples

If the list of words is`["eye", "eyes", "stick", "tick", "yes"]`, we can reconstruct the corrupted 
string `"eyestick"` in two possible ways, `"eyes tick"` and `"eye stick"`, so return `["eye stick", "eyes tick"]`. 
Note that even though `"yes"` is in the list of words, partial reconstructions do not count.

If the word list is `["a", "b", "ba"]`, and the corrupted string `"baba"`, we return `["b a ba",  "ba b a"]`. 
As`"ba ba"` would reuse the word `"ba"`, it is an invalid reconstruction.

### Test Cases

If you can compute these in a reasonable time, you are likely to have a correct solution.

```
whitespace("hellothere", ["hello"]) -> []
whitespace("low", ["er", "lower", "w", "wol"]) -> []
whitespace("aab", ["a", "aa", "ab"]) -> ["a ab"]
whitespace("cdd", ["c", "cd", "d"]) -> ["cd d"]
whitespace("ffff", ["f", "ff", "fff"]) -> ["f fff", "fff f"]
whitespace("dabcbda", ["a", "b", "bcb", "c", "d", "da"]) -> ["d a bcb da", "da bcb d a"]
whitespace("eyestick", ["e", "eye", "eyes", "stick", "tick", "yes"]) -> ["e yes tick", "eye stick", "eyes tick"]
whitespace("grandmashredderail", ["ail", "and", "ash", "derail", "era", "grand", "grandma", "mash", "rail", "ran", "red", "redder", "shred", "shredder"]) -> ["grand mash red derail", "grand mash redder ail", "grandma shred derail", "grandma shredder ail"]
whitespace("qwertyuiopasdfghjklzxcvbnm", ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "qw", "r", "s", "t", "u", "v", "w", "x", "y", "z"]) -> ["q w e r t y u i o p a s d f g h j k l z x c v b n m", "qw e r t y u i o p a s d f g h j k l z x c v b n m"]
```

### Things to Consider
 - Checking every possible placement of spaces does work, but... it would take a while. 
 - There's no constant time solution here - but we could check how the words fit into the string.
 - A longest-word-first approach fails. Why? What about a shortest-word-first one?
 - If we try building up from left to right and make a mistake, what should we do?

## ⭐⭐⭐⭐ Full Reconstruct

Okay, the test function was a success. Time for a real example. 
You open up one of the archived papers from the 90s - seems like they used write short stories. 
Not that you can tell, since it's been turned into a **corrupted** string.

You can find a copy of the text in this folder, in `archived_paper.txt`.

Well, what are you waiting for? Try to restore the original text, using a computer to help you!

### Things to Consider
- What are the similarities and differences compared to the last task? 
- Wouldn't it be great if there were some way to access all the words in the English language?
- Ah, but names of people and places won't show up there.
- What will happen to `I'm`, `won't` and `they're`?
- You don't need to fully automate the task, but see how much you can!

### Want more of a challenge? 
Create a function to convert a file into a corrupted string. 
Then, run the string through your reconstructor and check how close to the original it is!
You could also try dealing with an even longer piece of text (a lot of famous books are in the public domain).

