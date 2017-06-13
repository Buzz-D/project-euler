# -*- coding: utf-8 -*
# Berechne die Summe der Ziffern von 2^1000
# Antwort lautet 1366

n = 1000
product = str(2 ** n)
result = 0
for i in product:
    result += int(i)
print(result)
