f = open("25048321/9.txt")
f1 = []

for row in f:
    f1.append(list(map(int, row.split())))

c = 0


for row in f1:
    s = set(row)
    if len(s) == len(row) == 5:
        ma = max(row)
        mi = min(row)
        s1 = 2*(sum([mi, ma]))
        s2 = sum(row) - ma - mi
        if s1 <= s2:
            c += 1

print(c)

