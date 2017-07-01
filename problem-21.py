# -*- coding: utf-8 -*
# Wie lautet die Summe aller "Ammicable" Zahlen unter 10000
# Antwort lautet 31626
import primenumber


def find_sum_of_divisors(number):
    sod = 0
    primefactors = primenumber.primefactors(number)
    if not primefactors:
        return 1
    factors = [1]
    factors_temp = factors[:]
    for i in primefactors:
        for factor in factors:
            if i * factor not in factors:
                factors_temp.append(i * factor)
        factors = factors_temp[:]
    factors.remove(number)
    for i in factors:
        sod += i
    return sod


def main():
    ammicable = set()
    sum = 0
    for i in range(2, 10000):
        if i in ammicable:
            continue
        sod1 = find_sum_of_divisors(i)
        if sod1 == i:
            continue
        sod2 = find_sum_of_divisors(sod1)
        if i == sod2:
            ammicable.add(i)
            ammicable.add(sod1)
            sum += i + sod1
    print(sum)

main()

