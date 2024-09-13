#!/usr/bin/python3
def minOperations(n):
    if n <= 1:
        return 0  # No operations are needed if n is less than or equal to 1

    operations = 0  # Initialize operations to zero
    factor = 2  # Start by looking for the smallest prime factor

    # Continue only while n is greater than 1
    while n > 1:
        while factor <= n:  # Loop through all possible factors up to n
            if n % factor == 0:  # Check if factor divides n evenly
                operations += factor  # Add the factor to operations
                n //= factor  # Divide n by factor
            else:
                factor += 1  # Move to the next factor if the current factor doesn't divide evenly
    return operations  # Return the total number of operations after the loop completes

# Example usage:


print(minOperations(9))  # Output: 6
