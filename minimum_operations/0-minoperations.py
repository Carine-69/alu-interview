#!/usr/bin/python3
import os


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


test = [25, 1010110,120]  # List of test cases to evaluate

for i, case in enumerate(test):
    result = minOperations(case)  # Compute the result for the current test case

    filename = f"main-{i}.py"  # Create a filename based on the index of the test case

    with open(filename, "w") as file:
        file.write(f"Min number of operations to reach {case} characters:{result}\n")  # Write the string "result\n"
        # to the file

    print(f"Result of test case {case} is written to {filename}")
