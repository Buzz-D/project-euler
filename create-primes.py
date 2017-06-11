import io
import read_write


def find_primes(n):
    """ Returns  a list of primes < n """
    primes = [True] * n
    for i in xrange(3, int(n**0.5) + 1, 2):
        if primes[i]:
            primes[i*i::2*i] = [False] * ((n - i * i - 1) / (2 * i) + 1)
    result = [2] + [i for i in xrange(3, n, 2) if primes[i]]
    return result

primes = find_primes(1000000)
with io.open('primes.txt', 'w') as f:
    f.write(unicode(','.join(str(x) for x in primes)))
