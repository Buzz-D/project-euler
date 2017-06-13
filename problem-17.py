# -*- coding: utf-8 -*
# Wie viele Buchstaben kommen vor wenn man alle Zahlen von 1-1000 auflistet (Leerzeichen und Bindestrich zählen
# nicht. Englische Schreibweise)
# Antwort lautet 21124
import read_write

words = read_write.read_csv_file('problem-17.csv')
character_counter = 0
for i in range(1, 1001):
    if len(str(i)) == 1:
        character_counter += len(words[i])
    elif len(str(i)) == 2:
        if i in words:
            character_counter += len(words[i])
        else:
            single = int(str(i)[1])
            double = int(str(i)[0]) * 10
            character_counter += len(words[double]) + len(words[single])
    elif len(str(i)) == 3:
            triple = int(str(i)[0])
            character_counter += len(words[triple]) + len(words[100])
            if int(str(i)[1] + str(i)[2]) != 0:
                character_counter += 3
            if int(str(i)[1] + str(i)[2]) in words:
                character_counter += len(words[int(str(i)[1] + str(i)[2])])
            else:
                single = int(str(i)[2])
                double = int(str(i)[1]) * 10
                character_counter += len(words[double]) + len(words[single])
    else:
        character_counter += len(words[i]) + 3
print(character_counter)
