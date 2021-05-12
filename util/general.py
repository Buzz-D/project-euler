def find_factors(number):
    factors = set()
    for i in range(1, int(number ** 0.5)):
        if number % i == 0:
            factors.update([i, int(number / i)])
    if number % int(number ** 0.5) == 0:
        factors.add(int(number ** 0.5))
    return factors


def find_factors_length(number):
    factors = 0
    for i in range(1, int(number ** 0.5)):
        if number % i == 0:
            factors += 2
    if number % int(number ** 0.5) == 0:
        factors += 1
    return factors
