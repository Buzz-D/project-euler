# -*- coding: utf-8 -*
# Finde das größte Produkt vierer benachbarter Zahlen der Zahl aus der TXT Datei
# Antwort lautet 23514624000

import read_write

biggest_product = 0
number = read_write.read_file('problem-8.txt')
for i in range(len(number) - 12):
    product = 1
    for j in range(13):
        product *= int(number[i + j])
    if product > biggest_product:
        biggest_product = product
print(biggest_product)
