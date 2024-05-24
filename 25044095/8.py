import itertools

number = 0
rez = 0
for comb in itertools.product('АЗИМНОПРТ', repeat=5):
    number += 1
    if number % 2 == 0 and comb[0] == 'Н' and comb.count('Р') == 2:
        rez = number
        print(comb)
print(rez)