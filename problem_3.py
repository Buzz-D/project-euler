# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
from util.prime import find_prime_factors
import numpy, time


def main():
    number = 600851475143
    print(numpy.amax(find_prime_factors(number)[0]))


start_time = time.time()
main()
print("The runtime was %.2f seconds" % (time.time() - start_time))
