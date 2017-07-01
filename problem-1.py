# -*- coding: utf-8 -*
#  Finde die Summe aller Zahlen von 1 bis 1000 die ein vielfaches von 3 oder 5 sind
# Antwort lautet 233168

sum = 0
for number in range(1000):
    if number % 3 == 0 or number % 5 == 0:
        sum += number
print(sum)
