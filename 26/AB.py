f = open('26/26.txt')
l = []
m = 8200
for row in f:
    l.append(int(row))

l.sort()
s = []
# print(l)
for el in l:
    if sum(s) + el <= m:
        s.append(el)
print(s, sum(s), m + s[-1] -sum(s), len(s))