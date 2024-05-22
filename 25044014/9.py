f1 = open('25044014/9.txt')
f2 = open('25044014/9.1.txt', 'w')
f = []
number_and_quantity = {}
for row in f1:
    f.append(list(map(int, row.split())))
stroka = 0
for row in f:
    first = 0
    c = 0
    stroka += 1
    for i in range(len(row) - 1, 0, -1):
        if row[i] % 2 == 0:
            c += 1
        else:
            c = -10
        if c >= 3:
            first = 1
    if first:
        f2.write(str(stroka) + ' ' + ' '.join(list(map(str, row))))
        f2.write('\n')