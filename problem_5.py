# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
import time


def main():
    number = 1
    max_divisor = 20
    for i in range(1, max_divisor + 1):
        if number % i > 0:
            divisor = i
            while True:
                divisor *= i
                if divisor > max_divisor:
                    divisor /= i
                    break
            number *= divisor
    print("The smallest number evenly divisible by the number 1-20 is %d" % number)


start_time = time.time()
main()
print("The runtime was %.2f seconds" % (time.time() - start_time))
