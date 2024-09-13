#!/usr/bin/python3

def minOperations(n):
    """
    Calculate the minimum number of operations needed to achieve exactly n 'H' characters
    starting from one 'H' using Copy All and Paste operations.

    Parameters:
    n (int): The target number of 'H' characters.

    Returns:
    int: The minimum number of operations needed, or 0 if n is less than or equal to 1.
    """
    if n <= 1:
        return 0  # No operations are needed if n is less than or equal to 1

    operations = 0  # Initialize operations to zero
    factor = 2  # Start by looking for the smallest prime factor

    while n > 1:
        while factor <= n:  # Loop through all possible factors up to n
            if n % factor == 0:  # Check if factor divides n evenly
                operations += factor  # Add the factor to operations
                n //= factor  # Divide n by factor
            else:
                factor += 1  # Move to the next factor if the current factor doesn't divide evenly
    return operations

# Example test cases
test_cases = [4, 12]  # You can change or add more test cases as needed

for case in test_cases:
    result = minOperations(case)
    print(f"Min number of operations to reach {case} characters: {result}")