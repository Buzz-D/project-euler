# -*- coding: utf-8 -*
# Finde die Differenz der Summe der Quadradte von 1-100 und des Quadradts der Summe von 1-100
# Antwort lautet 25164150

square_of_sum = 0
sum_of_squares = 0
for number in range(1,101):
    sum_of_squares += number ** 2
sum_of_numbers = 50 * 101 #Trick ausnutzen statt alles aufzusummieren
square_of_sum = sum_of_numbers ** 2
print(int(square_of_sum - sum_of_squares))
