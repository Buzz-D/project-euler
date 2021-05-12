# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10001st prime number?
import time
from util.prime import is_prime


def main():
    count = 1  # 2 is already counted to make the while loop a bit cleaner
    i = 3  # the while loop directly starts at 3 to be able to have steps of 2 numbers
    last_prime = 2

    while True:
        if is_prime(i):
            count += 1
            last_prime = i
        if count == 10001:
            break
        i += 2
    print("The 10001 prime number is %d" % last_prime)


start_time = time.time()
main()
print("The runtime was %.2f seconds" % (time.time() - start_time))
