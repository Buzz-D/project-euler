import math


def is_prime(number):
    if number % 2 == 0 and number != 2:
        return False
    for i in range(3, math.isqrt(number) + 1, 2):
        if number % i == 0:
            return False
    return True


def find_prime_factors(number, primes):
    # Initialize variables
    number_temp = number
    i = 0
    prime_factors = [[], []]
    # Loop through all possible/needed primes
    while True:
        # The maximum prime can be number/2. E.g. 10=2*5 -> 5 is 10/2
        if primes[i] > (number / 2):
            break
        # Test how often the temporary number can be divided by the current prime
        number_temp = test_divisibility(number_temp, primes[i], prime_factors)
        if number_temp == 1:
            break
        i += 1
    # If the temporary number is larger then 1 at this point the number itself is a prime
    if number_temp > 1:
        prime_factors[0].append(number)
        prime_factors[1].append(1)

    return tuple(map(tuple, prime_factors))


def test_divisibility(number, divisor, factors):
    i = 0
    # Test if the number is divisible by the divisor
    if number % divisor == 0:
        # As long as the number is divisible do so and count how often this is possible
        while number % divisor == 0:
            number /= divisor
            i += 1
        # Add the divisor and the amount how often it divides to the factors
        factors[0].append(divisor)
        factors[1].append(i)
    # Return the new number that was divided
    return int(number)


def generate_primes(number):
    # Generate a simple list of primes up to the given number
    f = open("./prime_numbers.txt", "a")
    for i in range(3, number, 2):
        if is_prime(i):
            f.write("%d," % i)
    f.close()


def get_prime_numbers(limit=False):
    # Get the current list of primes
    # If you only need it till a specific point pass the maximum value as a parameter
    f = open("./prime_numbers.txt", "r")
    primes = tuple(map(int, f.read().split(",")))
    f.close()
    if limit:
        i = 0
        while True:
            if (limit + i) in primes:
                return primes[: primes.index(limit + i)]
            i += 1
    return primes
