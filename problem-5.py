# -*- coding: utf-8 -*
# Finde die kleinste Zahl, die durch die Zahlen 1-20 teilbar ist
# Antwort lautet 232792560

numbers_to_test = [5,7,9,11,13,16,17,19] #Alle Zahlen sind hierdurch abgedeckt
result = 1
for number in numbers_to_test:
    result *= number
print(result)