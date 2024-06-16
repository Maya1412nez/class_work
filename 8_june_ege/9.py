f = open('8_june_ege/9.txt')

l = []
for row in f:
    l.append(list(map(int, row.split())))

c = 0
for row in l:
    three = set()
    one = set()
    for el in row:
        if row.count(el) == 3:
            three.add(el)
        if row.count(el) == 1:
            one.add(el)
    if len(three) == 1 and len(one) == 3:
        if (int(list(three)[0]) * 3) ** 2 > sum(list(one)) ** 2:
            print(row, one, three)
            c += 1
print(c)