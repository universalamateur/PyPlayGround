#!/usr/bin/env python3

import time

"""Find all rPrimes till a curtain given integer as upper barrier
"""

def primes_list(n):
    """
    input: n an integer > 1
    returns: list of all the primes up to and including n
    """
    # initialize primes list
    primes = [2]
    # go through each of 3...n
    for j in range(3,n+1):
        is_div = False
        # go through each elem of primes list
        for p in primes:
            if j%p == 0:
                is_div = True
                break
        if not is_div:
            primes.append(j)
    return primes

def main():
    #Upper_Stop=int(input("Please enter a positive number greater than 1: "))
    Upper_Stop = 555555
    start_time = time.time()
    list_of_primes = primes_list(Upper_Stop)
    print(f"The list of prime numbers until the given value {Upper_Stop} is : {list_of_primes}")
    end_time = time.time()
    print(f"Number of primes found: {len(list_of_primes)}")
    print(f"Runtime of this calculation was {end_time - start_time}")

if __name__ == "__main__":
    main()
