f = open('25044384/17.txt')
l = []
m = 0
mi = 10000000
c = 0
for row in f:
    l.append(int(row))
    if int(row) % 141 == 0 and m < int(row):
        m = int(row)

for i in range(len(l) - 2):
    tripple = [l[1], l[i+1], l[i+2]]
    sums = set()
    for el in tripple:
        s = 0
        for letter in str(el):
            s += int(letter)
        sums.add(s)
    if len(sums) == 3 and sum(tripple) > m:
        c += 1
        if mi > sum(tripple):
            mi = sum(tripple)
print(c, mi)

