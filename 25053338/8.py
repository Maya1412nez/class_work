import itertools

num = 0
c = 0
for comb in itertools.product('АПРСУ', repeat=5):
    num += 1
    f = 0
    if comb.count('У') <= 1:
        for i in range(len(comb)-1):
            if comb[1] == comb[i+1] == 'А':
                f = 1
                break
        if f == 0:
            c = num
            print(''.join(comb), c)

print(c)
