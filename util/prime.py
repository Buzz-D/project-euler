import math


def is_prime(number):
    if number % 2 == 0 and number != 2:
        return False
    for i in range(3, math.isqrt(number) + 1, 2):
        if number % i == 0:
            return False
    return True


def find_prime_factors(number):
    prime_factors = []
    test_divisibility(number, 2, prime_factors)
    for i in range(3, math.isqrt(number) + 1, 2):
        if is_prime(i):
            number, prime_factors = test_divisibility(number, i, prime_factors)
        if number == 1:
            break
    return prime_factors


def test_divisibility(number, divisor, factors):
    while number % divisor == 0:
        factors.append(divisor)
        number /= divisor
    return number, factors
