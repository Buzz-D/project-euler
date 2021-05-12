# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

import time


def main():
    sum_of_multiples = 0
    for i in range(3, 1000):
        if i % 3 == 0:
            sum_of_multiples += i
            continue
        elif i % 5 == 0:
            sum_of_multiples += i
    print("The sum of all multiples of 3 and 5 below 1000 is %d" % sum_of_multiples)


start_time = time.time()
main()
print("The runtime was %.2f seconds" % (time.time() - start_time))
