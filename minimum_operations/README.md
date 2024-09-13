## minOperations Function Documentation

This script defines a function `minOperations(n)` that calculates the minimum number of operations to achieve exactly `n` 'H' characters in a file, starting with one 'H', using only Copy All and Paste operations.

### Usage
The function takes an integer `n` as input and returns the minimum number of operations needed.

- If `n <= 1`, it returns `0`, as no operations are needed.
- Otherwise, it finds the prime factors of `n` and calculates the minimum number of operations.

Example:
n = 9 
H => Copy All => Paste => HH => Paste =>HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH