# Chess With Holes
**Difficulty Range**: ⭐ - ⭐⭐
**Tags**: `chess`, `2d-grids`, `modular-arithmetic`

We have an `8`x`8` board. Each cell of this board is represented from `0`-`63` as below

|     |     |     |     |     |     |     |     |     |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|     | 56  | 57  | 58  | 59  | 60  | 61  | 62  | 63  |
|     | 48  | 49  | 50  | 51  | 52  | 53  | 54  | 55  |
|     | 40  | 41  | 42  | 43  | 44  | 45  | 46  | 47  |
|     | 32  | 33  | 34  | 35  | 36  | 37  | 38  | 39  |
|     | 24  | 25  | 26  | 27  | 28  | 29  | 30  | 31  |
|     | 16  | 17  | 18  | 19  | 20  | 21  | 22  | 23  |
|     |  8  |  9  | 10  | 11  | 12  | 13  | 14  | 15  |
|     |  0  |  1  |  2  |  3  |  4  |  5  |  6  |  7  |

A *sliding piece* is a piece that can move along certain directions until it hits the boundary of the board. This question is all about sliding pieces.

## ⭐ Rooks, Bishops and Queens
What you need to do is create a function that takes in three arguments, `piece_type`, `start` and `end`, the indices of a potential move, and return whether that piece can make that move or not.

**Rooks** can move up, down, left or right. This should be familiar if you've played Chess. For example:
 - `can_move("rook", 0, 32) -> true` because rooks can move vertically up the board.
 - `can_move("rook", 10, 27) -> false` because there's no possible way to make that move by only moving up, down, left or right.

**Bishops** can diagonally. For example:
 - `can_move("bishop", 25, 52) -> true` because bishops can move diagonally up and to the right.
 - `can_move("bishop", 14, 54) -> false` because there's no possible way to make that move by only moving diagonally.

**Queens** can like a rook and bishop combined. For example:
 - `can_move("queen", 25, 52) -> true` because queens can move diagonally up and to the right.
 - `can_move("queen", 0, 32) -> true` because queens can move vertically up the board.

## ⭐⭐Holes
The chess board we're using was poorly manufactured. As a result, squares are falling out of it!

We now introduce another argument: a list of those indices that do not exist, also known as holes. You'll need to take them into account. Rooks and bishops can't jump over holes. They're a bit like the boundary of the board.

Now, add to _this_ function so that it takes holes into account by accepting the list of holes as a fourth argument. For example:

`can_move("rook", 6, 30, [22, 45, 32]) -> false` because cell `22` is missing, blocking a rook moving from `6` to `30`.

The holes list may be empty.

## ⭐⭐ Deduction

Create a function `deduce_hole` that 2 arguments in the form below (This represents that there is a rook on  cell `45` and a bishop on cell `32`):
```
deduce_hole(
	["rook", 45],
	["bishop", 32]
)
```

And, given that both pieces can be blocked by the same hole, returns all possible cell numbers for the hole to be on .

### Examples
```
deduce_hole(
	["rook", 45],
	["bishop", 32]
)
```
would return `[41]`: if `41` was a hole, it would stop the bishop at `32` when he moved up and to the right, and it would also stop the rook at `45` when he went left. There are no other possible holes that can block both pieces in any of their directions. However,

```
deduce_hole(
	["rook", 45],
	["bishop", 35]
)
```

would return `[44, 42, 53, 21]`: They can all block both pieces at the same time.


