# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# Pythagorean triplets can be found by applying the following formular:
# x=u^2-v^2 , y=2uv , z=u^2+v^2
# This leads to 1000 = x + y + z = 2u^2 + 2uv
# -> v = 1000 / 2u - u
# With this we get the following algorithm

import time


def main():
    sum_of_triplet = 1000
    u = 1
    while True:
        v = (sum_of_triplet / (2 * u)) - u
        if v.is_integer():
            x = u ** 2 - v ** 2
            y = 2 * u * v
            z = u ** 2 + v ** 2
            if x > 0 and y > 0 and z > 0:
                break
        u += 1
    print(
        "The product of the triplet is %d with x = %d, y = %d and z = %d"
        % (x * y * z, x, y, z)
    )


start_time = time.time()
main()
print("The runtime was %.2f seconds" % (time.time() - start_time))
