# -*- coding: utf-8 -*
# Wie lautet die Summe der Ziffern von 100!
# Antwort lautet 648

import math

n = 100
factorial = str(math.factorial(n))
sum = 0
for n in factorial:
    sum += int(n)
print(sum)
