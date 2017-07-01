# -*- coding: utf-8 -*
# Wie viele Monate fingen zwischen 1901 und 2000 mit einem Montag an
# Antwort lautet 171

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = 366 # Die 365 Tage des ersten Jahres (kein Schaltjahr!)
counter = 0
for i in range(1, 101):
    for month in months:
        days += month
        if month == 28 and i % 4 == 0:
            days += 1
        if days % 7 == 0:
            counter += 1
print(counter)
