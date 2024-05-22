from itertools import *

s = 0
for comb in permutations('0123456789', r=6):
    f = 0
    if comb[0] != '0':
        if int(''.join(comb)) % 5 == 0:
            for i in range(len(comb) - 1):
                if (int(comb[i]) % 2) == (int(comb[i+1]) % 2):
                    f = 1
            if f == 0:
                s += 1
                # print(int(''.join(comb)))
print(s)
