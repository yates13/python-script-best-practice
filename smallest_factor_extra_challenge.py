#! /usr/bin/env python3

"A module for getting the smallest prime factor of an integer."

import sys

#extra assignment part one
def get_smallest_prime_factor(n):
    """Returns the smallest prime number that is a divisor of n"""
    # Start checking with 2, then move up one by one
    i = 2
    while i*i <= n:
        if n % i == 0:
            return i
        i += 1
    return n
    var = get_smallest_prime_factor(n)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(sys.argv[0] + ": Expecting one command line argument -- the integer for which to get the smallest factor")
    n = int(sys.argv[1])
    if n < 1:
        sys.exit(sys.argv[0] + ": Expecting a positive integer")

    smallest_prime_factor = get_smallest_prime_factor(n)

    if smallest_prime_factor is None:
        print(n)
    else:
        print(smallest_prime_factor)
