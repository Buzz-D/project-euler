# -*- coding: utf-8 -*
# Finde das größte Produkt vierer aneinanderliegender Zahlen
# Antwort lautet 70600674

import read_write

biggest_product = 0
counter = 0
numbers = read_write.read_csv_file('problem-11.csv')
# Checke Links Rechts
for i in range(len(numbers)):
    for j in range(len(numbers[i]) - 3):
        product = int(numbers[i][j]) * int(numbers[i][j + 1]) * int(numbers[i][j + 2]) * int(numbers[i][j + 3])
        if product > biggest_product:
            biggest_product = product
# Checke Oben Unten
for i in range(len(numbers) - 3):
    for j in range(len(numbers[i])):
        product = int(numbers[i][j]) * int(numbers[i + 1][j]) * int(numbers[i + 2][j]) * int(numbers[i + 3][j])
        if product > biggest_product:
            biggest_product = product
# Checke Diagonal 1
for i in range(len(numbers) - 3):
    for j in range(len(numbers[i]) - 3):
        product = int(numbers[i][j]) * int(numbers[i + 1][j + 1]) * int(numbers[i + 2][j + 2]) * int(numbers[i + 3][j + 3])
        if product > biggest_product:
            biggest_product = product
# Checke Diagonal 2
for i in range(len(numbers) - 3):
    for j in range(len(numbers[i]) - 3):
        product = int(numbers[i + 3][j]) * int(numbers[i + 2][j + 1]) * int(numbers[i + 1][j + 2]) * int(numbers[i][j + 3])
        if product > biggest_product:
            biggest_product = product
print(biggest_product)
