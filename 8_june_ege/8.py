import itertools
c = 0
for comb in itertools.product('КОСУФ', repeat=5):
    c += 1
    if 'Ф' not in comb and comb.count('У') == 2:
        print(c, comb)
