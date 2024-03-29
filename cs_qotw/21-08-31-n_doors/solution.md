# The N-Doors Problem - Solution
**Difficulty Range**: ⭐ - ⭐⭐
**Tags**: `n-doors`, `iteration`

The solutions to The N-Doors Problem.

## ⭐ N-Passes
A naive algorithm may be something like this, manually toggling every door:

 - Create an array of length `N`, filled with `False`.
 - For `i` from `1` to `N`:
   - Look at every `i`th element in the array. Turn that `True` into a `False`, and vice versa.
 - Loop through the array to find the highest number still open and return it.

This is fine for small `N`, but for very large `N` it's inefficient. However, there is a pattern you can spot to solve this question better. Let's show the first `15` solutions:

| `N`                       | Answer |
|:------------------------- |:------:|
| 1, 2, 3                   |   1    |
| 4, 5, 6, 7, 8             |   4    |
| 9, 10, 11, 12, 13, 14, 15 |   9    |

There's a pattern here - the answer seems to be the largest square number less than or equal to `N`. Let's explain this pattern.

First, realise that a door `n` is toggled on every pass `k` where `k` is a factor of `n`. If you're visiting every `k`th door and `k` is a factor of `n` then you'll surely land on door `n`. So,

> A door is toggled as many times as it has factors.

Every non-square number has an even number of factors. `2` is a factor of `18`, because `2` × `9` = `18`.  But this also means that `9` is a factor. They come in pairs `a` × `b`, where `a` and `b` are distinct, so each such pair contributes two factors. But square numbers are an exception. For every square number `S` there is also some integer `a` where `a` × `a` = `S`. That is the definition of a square number. This last pair is only one unique factor though, so square numbers have an odd number of factors.

> All square numbers have an odd number of factors, and all other positive integers have an even number of factors.

If a door has an even number of factors, it's going to stay closed. Every two toggles will cancel each other out. If it has an odd number of factors, it's going to be open -- the last toggle isn't cancelled out by anything. This means that for some integer `N`, all doors that are square numbers `<= N` will be open.

Now, we just need to find the largest square number `<= N`. How can we do that? We could square root `N`, round down, and then square it again. Here is some pseudocode:
```
func n_doors(n: int): int
    return n.sqrt().floor().pow(2)
end func
```

This is much faster than the naive approach.

---

For the bonus question about efficiently finding *how many* doors are open at the end, we just find the floor of `sqrt(N)`. This is because if there's some positive integer `a` where `a^2 <= N`, then every positive integer `< a` will also square to give a square number `< N`. This means that if `a` is the floor of `sqrt(N)`, then it's also the number of squares `<= N`, so that's how many doors would be open.

 - The **floor** of a number is that number rounded down. The floor of `4.9` is `4`.
 - The **ceiling** of a number is that number rounded up. The ceiling of `6.1` is `7`.

---

The pseudocode is the same as above but without the `.pow(2)`.

## ⭐⭐ Prime Watch
As a naive solution, you might write an algorithm like this:
 - Create an array of length `N`, filled with `False`.
 - For every prime number `i <= N`:
	 - For every positive power of `i` (call that `j`) `<=N`:
	 	- Toggle every `j`th door.
 - Return the value of the last element in the array.

This works alright for small `N` but is infeasible for larger `N`. Even if we be smart and only store the state of the `N`-th door, the algorithm is still very slow. There is, again, a neater solution. Let's try explaining it.

As we've shown in _⭐ N-Passes_, you're only going to be toggling the `N`th door on every pass `k`, where `k` is a factor of `N`.

If we're visiting every `k`th door where `k` is a power of a prime, then a door is going to be toggled as many times as it has prime factors: for every `x^n` term in its prime factorisation, it's going to be toggled `n` times for that `x`. Every power of `x` up to and including `n` is a factor, so they'd all toggle `N`. Therefore, the number of times a door gets toggled is the number of prime factors of that number, _counted with multiplicity_ (i.e. if a number has a `2^7` in its factorisation that's `7` factors.)

> A door number will be open by the end if it has an odd number of prime factors, and closed if it has an even number of prime factors, **counted with multiplicity**.

How does this look as some pseudocode?
```
func is_open(n: int): bool:
	factors = 0 // How many prime factors in `n`
	curr_factor = 2 // Current number we're checking is a factor

	while curr_factor <= sqrt(n).ceil():
		if n % curr_factor == 0:
			n /= curr_factor
			factors += 1
		else:
			curr_factor += 1
	return factors % 2 != 0
end func
```

One thing you may notice is that `curr_factor` only needs to check prime factors: `n  % curr_factor == 0` will always be `False` when `curr_factor` is a composite number, because they are the product of two or more smaller numbers. Assuming you're iterating in increasing order, these smaller factors will have been divided out already. The only numbers that won't certainly be `False` are prime numbers, so we only need to iterate over those.

You can use any method you know to generate prime numbers up to `sqrt(n)`, but for a simple way to increase the proportion of numbers that you check being prime, you can divide by `2` first as many times as needed, and then check from `3` but skipping every even number, as all even numbers `> 3` are certainly not prime. This optimisation is possible because all `2`s have been divided by, so no even number can possibly be a factor. This reduces the number of integers to check from `sqrt(N)` to `sqrt(N) / 2`. There are other methods possible, such as a seive: see the [Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes) for a popular example.