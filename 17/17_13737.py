f = open('17/17_13737.txt')

l = []
m = 0
c = 0
for row in f:
    l.append(int(row))
    if str(int(row))[-3:] == '221':
        m = max(m, (int(row)))
    # print(str(int(row))[-3:])
print(m)

mi = 9999999999999999999999999999999
for i in range(len(l) - 2):
    tr = l[i:i+3]
    f1 = 0
    f2 = 0
    for el in tr:
        if len(str(abs(el))) > 1 and str(el)[-2] in '13579':
            f1 += 1
            # print(el)
        if len(str(abs(el))) == 2:
            f2 += 1
            # print(el)
    if f1 == 2 and f2 <= 2 and sum(tr) > m:
        print(tr, m, sum(tr))
        c += 1
        mi = min(sum(tr), mi)
print(c, mi)