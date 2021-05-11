# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


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
print(int(number))
