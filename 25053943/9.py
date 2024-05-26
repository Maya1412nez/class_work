f = open('25053943/9.txt')
l = []
for row in f:
    l.append(list(map(int, row.split())))
# print(l, len(l))
c = 0
for row in l:
    f = 0
    if max(row) ** 2 == (min(row) ** 2 + (sum(row) - min(row) - max(row)) ** 2):
        f = 1
        # print(row)
    for el in row:
        if all(int(str(el)[-1]) > 7 for el in row):
            f = 1
    if f:
        c += 1
print(c)