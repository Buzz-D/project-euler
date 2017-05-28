# -*- coding: utf-8 -*
# Finde die größte Palindromzahl aus einem Produkt zweier dreistelliger Zahlen
# Antwort lautet 906609

import time


def main():
    largest_palindrom = 0
    for number1 in range(999, 100, -1):
        for number2 in range(999, 100, -1):
            product = number1 * number2
            if product > largest_palindrom:
                #print(product)
                #print(len(product))
                product_as_string = str(product)
                reverse = ''
                for i in range(len(product_as_string)):
                    reverse += product_as_string[len(product_as_string) - 1 - i]
                    #print(reverse)
                if product_as_string == reverse:
                    largest_palindrom = product
    print(largest_palindrom)


start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))