# -*- coding: utf-8 -*
# Finde die Summe aller Primzahlen unter 2000000
# Antwort lautet 142913828922

import primenumber

sum_of_primes = 2 #Die erste Primzahl wird zur Einfachheit halber direkt angegeben
for number in range(3, 2000000, 2):
    if primenumber.isPrime(number):
        sum_of_primes += number
print(sum_of_primes)