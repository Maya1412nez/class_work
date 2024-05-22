import itertools

c = 0
counter = 0
for comb in itertools.product('АИНПТЦЯ', repeat=6):
    c += 1
    if c % 2 == 0:
        if comb[0] != 'Н':
            if comb.count('Я') == 2:
                counter += 1
                # print(''.join(comb))
print(counter)