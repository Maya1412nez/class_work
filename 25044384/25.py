import fnmatch

l = []
d = dict()
for i in range(2024, 10**10, 2024):
    s = 0
    for el in str(i):
        s += int(el)
    if s % 2 == 1:
        if fnmatch.fnmatch(str(i), '112?57*4'):
            l.append(i)
            d[i] = i / 2024

l1 = sorted(l)
for el in l1:
    print(d[el])
print(d)