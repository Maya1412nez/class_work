import itertools

c = 0
for comb in itertools.permutations('0245678', r=6):
    if comb[0] != '0':
        f = 0
        for i in range(len(comb) - 1):
            if int(comb[i]) % 3 == int(comb[i+1]) % 3 == 0:
                f = 1
                break
        if not f:
            print(''.join(comb))
            c += 1
    
print(c)