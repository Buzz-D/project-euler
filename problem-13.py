# -*- coding: utf-8 -*
# Berechne die ersten 10 Ziffern der Summe der 100 Zahlen in der txt Datei
# Antwort lautet 5537376230

import read_write

numbers = list(map(int, read_write.read_file("problem-13.txt")))
result = 0
for number in numbers:
    result += number
result_str = ""
for i in range(10):
    result_str += str(result)[i]
print(result_str)