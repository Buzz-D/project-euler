# -*- coding: utf-8 -*
# Finde die Summe aller geraden Fibonacci Zahlen bis 4 Millionen
# Antwort lautet 4613732

fib_sum = 2
fib1 = 1
fib2 = 2
fib_temp = 0
while fib_temp <= 4000000:
    if fib_temp % 2 == 0:
        fib_sum += fib_temp
    fib_temp = fib1 + fib2
    fib1 = fib2
    fib2 = fib_temp
print(fib_sum)
