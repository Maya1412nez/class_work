f = open('25044095/9.txt')
l = []
for row in f:
    l.append(list(map(int, row.split())))

c = 0
for row in l:
    if len(set(row)) == len(row):
        smima = (max(row) + min(row)) * 2
        s_ost = (sum(row) - max(row) - min(row)) * 3
        if smima <= s_ost:
            c += 1
            print(row, smima, s_ost)
print(c)
