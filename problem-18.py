# -*- coding: utf-8 -*
# Berechne den Pfad mit der höchsten Summe
# Antwort lautet 1074
import io

with io.open('problem-18.txt', 'r') as f:
    content = f.readlines()
    numbers = [list(map(int, x.strip('\n').split(' '))) for x in content]
sum_tree = numbers
for i in range(1, len(numbers)):
    for j in range(len(numbers[i])):
        if j == 0:
            sum_tree[i][j] += numbers[i-1][j]
        elif j == len(numbers[i]) - 1:
            sum_tree[i][j] += numbers[i-1][j-1]
        else:
            sum_tree[i][j] += max(numbers[i-1][j-1], numbers[i-1][j])
print(max(sum_tree[-1]))

