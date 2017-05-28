#Funktionen vom Einlesen und Schreiben von Zahlen

import csv
import io


def read_file(file_to_read):
    with io.open(file_to_read, 'r') as stream:
        content = stream.read()
    return content


def read_primenumbers_from_file(file_to_read):
    numbers = []
    with open(file_to_read, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:
            numbers.append(row)
        return numbers


def write_primenumber_to_file(number, file_to_write):
    with open(file_to_write, 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(number)
