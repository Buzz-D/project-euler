# Generelle Funktionen im Bezug auf Primzahlen
import csv
import math


def primefactors(number):
    factors = []
    while number % 2 == 0:
        number /= 2
        factors.append(2)
        if number == 0:
            return factors
    for i in range(3, int(math.sqrt(number)) + 2):
        if isPrime(i):
            while number % i == 0:
                number /= i
                factors.append(i)
                if number == 1:
                    return factors


def isPrime(number):
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


def getPrimes():
    return

def addPrime(prime):
    return
