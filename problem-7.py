# -*- coding: utf-8 -*
# Finde die 10001 Primzahl
# Antwort lautet 104743

import primenumber

prime_counter = 1
number = 1
while prime_counter < 10001:
    number += 2
    if primenumber.isPrime(number):
        prime_counter += 1
print(number)
