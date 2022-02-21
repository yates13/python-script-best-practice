#! /usr/bin/env python3

"A module for getting all prime factors"
import sys
import smallest_factor

"Assigning user input to a variable"
n = int(sys.argv[1])

if __name__ == '__main__':
    var = smallest_factor.get_smallest_prime_factor(n)
    print(var)


