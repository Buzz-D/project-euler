# -*- coding: utf-8 -*
# Finde das Pythagoreische-Tripel welches 1000 ergibt und berechne dessen Produkt
# Antwort lautet 31875000

product = 0
for a in range(1, 333):
    for b in range(a + 1, (1000 - a) / 2):
        c = 1000 - a - b
        if pow(a, 2) + pow(b, 2) == pow(c, 2):
            product = a * b * c
            break
    if product != 0:
        break
print(product)
