# -*- coding: utf-8 -*
# Finde die erste Triangle Zahl mit mehr als 500 Teilern
# Antwort lautet 76576500

import math
import time
import read_write


def find_number_of_divisors(number, primes):
    nod = 1
    number_temp = number
    for prime in primes:
        if prime > math.sqrt(number) or prime > number_temp:
            break
        pf = 0
        while number_temp % prime == 0:
            pf += 1
            number_temp /= prime
        nod += pf * nod
    return nod


def main():
    number = 1
    counter = 2
    primes = list(map(int, read_write.get_primes()))
    while find_number_of_divisors(number, primes) < 500:
        number += counter
        counter += 1
    print(number)

start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))