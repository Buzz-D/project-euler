# -*- coding: utf-8 -*
# Finde die größte Collatz Kette unter 1000000
# Antwort lautet 837799
import time


def even(number):
    return number / 2


def odd(number):
    return 3 * number + 1


def main():
    max_length = 0
    max_number = 0
    nos = {}
    for number in xrange(2, 1000000):
        lon = [number]
        counter = 1
        if number in nos:
            continue
        while number is not 1:
            if number % 2 == 0:
                number = even(number)
            else:
                number = odd(number)
            lon.append(number)
            counter += 1
            if number in nos:
                counter += nos[number] - 1
                break
        for i in xrange(len(lon)):
            nos[lon[i]] = counter - i
        if counter > max_length:
            max_length = counter
            max_number = lon[0]
    print(max_number, max_length)

start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))