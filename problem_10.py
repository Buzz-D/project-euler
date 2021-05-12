# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

import time
from util.prime import is_prime


def main():
    max_range = 2000000
    sum_of_primes = 2  # Already added the 2 so that only every second number can be checked for being a prime
    for i in range(3, max_range, 2):
        if is_prime(i):
            sum_of_primes += i
    print("The sum of all primes below %d is %d" % (max_range, sum_of_primes))


start_time = time.time()
main()
print("The runtime was %.2f seconds" % (time.time() - start_time))
