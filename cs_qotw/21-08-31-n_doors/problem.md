# The N-Doors Problem
**Difficulty Range**: ⭐ - ⭐⭐
**Tags**: `n-doors`, `iteration`

_This question is split into two parts -- try ⭐ N-Passes, and then for a greater challenge, try ⭐⭐ Prime Watch._

## ⭐ N-Passes
There are `N` doors, indexed starting at `1`. They're all initially closed. You make `N` passes of the doors. 

Pass `1`: *toggle* every door (close a door if open, and open it if closed).
Pass `2`: toggle every second door (`#2`, `#4`, `#6` etc.)
Pass `3`: toggle every third door (`#3`, `#6`, `#9` etc.)
Pass `N`: toggle only the `N`th door.

What is the highest door number open after these passes?

### Example
```
n_doors(4) -> 4
```

| Pass | Door 1 | Door 2 | Door 3 | Door 4 |
|:----:|:------:|:------:|:------:|:------:|
|  0   | Closed | Closed | Closed | Closed |
|  1   |  Open  |  Open  |  Open  |  Open  |
|  2   |  Open  | Closed |  Open  | Closed |
|  3   |  Open  | Closed | Closed | Closed |
|  4   |  Open  | Closed | Closed |  Open  |

`4` is the largest door number open by the end, so that's the answer.

### Things to Consider
 - Try optimising for size. What's the smallest you can get your program?
 - There's a neat trick to make this problem easier and more efficient than a naive approach. Can you work it out? Further, can you explain _why_ this method works?
 - As a side problem, can you also work out a similar trick to find the **number** of doors open at the end, instead of a naive approach? Further, can you explain _why_ this method works? This shouldn't be too difficult if you have managed to explain the above part.

### Efficiency of Your Algorithm
Test your algorithm against the following cases. If it can compute all of these in reasonable time, you very likely have the most efficient solution.
```
n_doors(4) -> 4
n_doors(554) -> 529
n_doors(3577) -> 3481
n_doors(24649) -> 24649
n_doors(101494432) -> 101485476
n_doors(975086612364448) -> 975086558093376
n_doors(753589263291372528) -> 753589262373516864
```

## ⭐⭐ Prime Watch
You come back and find all the doors are closed again. It turns out that the hotel is actually managed by the prime numbers, and they weren't too happy that some of the passes you were making were composite! Now the prime numbers take turns being on guard duty - banning you from toggling doors ever again yourself. On day `k`, the `k`th prime number is on guard duty. Call that prime number `G`. `G` calls up all the powers of `G` (e.g. `2` phones up `2`, `4`, `8`, `16`, `32`, etc.) and asks them to each, in turn, go round and toggle all doors that are a multiple of their number. So if `N = 17`,  then on `2`'s day of guard duty:

 - `2` toggles all the even numbers between `1` and `17`
 - `4` toggles all the multiples of `4` between `1` and `17`
 - `8` toggles all the multiples of `8` between `1` and `17`
 - `16` toggles just their own door.

The next day, `3`, as the next prime number, takes over, and this process repeats with the powers of `3`.

Create a function to work out, for a given `N`, whether door `N` will be open.

### Things To Consider
 - Try optimising for size. What's the smallest you can get your program?
 - Again, there's a trick that will get you a more efficient solution than the naive approach. Can you find it? 

### Test Cases
Here are some test cases. Again, if you manage to compute the last one in reasonable time, you very likely have the most efficient solution.
```
is_open(6) -> false
is_open(7) -> true
is_open(345) -> true
is_open(5432) -> true
is_open(1023045) -> false
is_open(2048349304) -> false
is_open(983048596023) -> true
```