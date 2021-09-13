# Reconstruct - Solutions

## ⭐⭐⭐ Whitespace

A naive algorithm would generate strings of all possible whitespace positions,
then check each to see if it uses the words correctly. As you might imagine, this is inefficient.
If the input string were `n` characters long, we would have to check `2^(n-1)` spacings!  

Clearly, we should instead be using the approach of trying to check if words can 'slot' into the string.
Since we need to check all possibilities, it makes sense to use a recursive, backtracking approach (as the tags suggest).

 - Create two functions, one non-recursive, the other recursive. 
 - Have the first function call the second with the same arguments.
 - If the input string to the recursive function is empty, we return `[""]`.
 - Otherwise, create an empty spacings list, and for all string prefixes:
   - If the prefix is in the words list:
     - Call the same function on the remaining string and words.
     - Append to the spacings list all suffixes, with the prefix and a space in front.
 - Return the spacings list (this may be empty).
 - Once the recursion has ended, format the output.

There is a sample solution in this folder, `whitespace.py`, which passes the test cases. There are still a number of
things that could be done to improve it, such as storing the words in a dictionary for faster access, 
or exploiting early exit conditions.

Ironically, the worst case input scenario still makes this algorithm perform terribly,
even though on average and for real words it performs much better. What sort of input do you think this might be?

## ⭐⭐⭐⭐ Full Reconstruct

This was more of an open-ended question. If you really wanted to, you could have just read the full string yourself. 
But that's boring, and kinda misses the point. Firstly, we need to ask ourselves: what changed from the last part?

Firstly, we're not given any words to work with! Thankfully, we don't have to produce every possible valid 
reconstruction though - just one should suffice. Looks like we'll have to find a list of English words, 
such as [this](https://github.com/dwyl/english-words) one. 
It would be a good idea to place them all in a dictionary for easy access.

Secondly, we're dealing with a significantly longer string. 
As such, it wouldn't be very practical to search the entire string to identify a single word.
You could limit the search by somewhere between 10-20 characters per word at most, and avoid backtracking on common 
shorter words by taking the longest prefix first.

Thirdly, we need to consider that not everything will be inside this dictionary. 
For example, names or places aren't likely to be included in our English word list. 
Additionally, numbers should be treated separately. Any word containing a `'` will be missed. 
One solution would be to skip over characters in a prefix when we can't identify it, and add whitespace according to 
the characters skipped.

Combining these three things should reveal the true article fairly well!

---

If you really want to try and reconstruct the punctuation and capitalisation, this is where it gets tricky.
This time it might be useful to tag words according to what type they are, such as noun, verb or adjective.
Not only would you get a speedup from being able to remove invalid sentence structure - 
but it may be possible to determine where certain punctuation markers like `,` and `.` would go.

Here's a hint: There are 60 sentences!