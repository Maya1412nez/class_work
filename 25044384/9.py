f = open('25044384/9.txt')
f1 = []
for row in f:
    f1.append(list(map(int, row.split())))

c = 0
for row in f1:
    f = 0
    povt = 1
    nepovt = []
    for i in range(len(row) - 1):
        if (row[i] % 2) == (row[i+1] % 2):
            f = 1
    for i in range(len(row)):
        if row.count(row[i]) > 1:
            povt *= row[i]
        else:
            nepovt.append(row[i])
    if povt == 1:
        povt = 0
    
    if 3 * sum(nepovt) >= povt and f == 0:
        c += 1 + i

print(c)