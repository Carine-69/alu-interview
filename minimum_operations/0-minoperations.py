#!/usr/bin/python3
def minOperations(n):
    if n <= 1:
        return 0

    operations = 0  # initialise operations to zero
    factor = 2  # find ll factors string from the smallest prime factor
    while n > 1:    # continue only if n is greater than one
        while factor <= n:  # factor can be any number less or equal to n which can divide
            if n % factor == 0:  # we keep dividing by factor(smallest factor) until n becomes 1
                operations += factor    # after getting first factor , we add it to operations
                n //= factor    # this takes the remainder from n after division and divide it again by the factor(
                # smallest divisor)
                factor += 1  # this is to increment factor in order to find the next divisor of n
                return operations


