# -*- coding: utf-8 -*
# Finde die erste Triangle Zahl mit mehr als 500 Teilern
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