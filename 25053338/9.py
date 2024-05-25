import itertools

f = open('25053338/9.txt')
l = []
for row in f:
    l.append(list(map(int, row.split())))
c = 0
for row in l:
    f = 0
    if max(row) < (sum(row) - max(row)):
        for comb in itertools.permutations(row):
            # print(comb[:2], comb[2:], sum(comb[:2]), sum(comb[2:]))
            if sum(comb[:2]) == sum(comb[2:]):
                f = 1
        
        if f:
            c += 1
print(c)

