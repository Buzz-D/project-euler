#Funktionen vom Einlesen und Schreiben von Zahlen

import csv
import io


def read_file(file_to_read):
    with io.open(file_to_read, 'r') as stream:
        content = stream.readlines()
        content = [x.strip('\n') for x in content]
    return content


def read_csv_file(file_to_read):
    content = []
    with open(file_to_read, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in reader:
            content.append(row)
        return content


def get_primes():
    with io.open('primes.txt', 'r') as f:
        primes = f.read().split(',')
        #primes.pop()
        return primes


def write_primenumber_to_file(numbers, file_to_write):
    with open(file_to_write, 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(numbers)
