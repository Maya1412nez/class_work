f = open('17/17_14952.txt')
l = []
m = 0
for row in f:
    l.append(int(row))
    # print(int(row[-4:]))
    if int(row[-4:]) == 121 and int(row) > m:
        m = int(row)
print(m)
c = 0
m_s = 0
for i in range(len(l) - 2):
    tripple = l[i:i+3]
    # print(tripple)
    f = 0
    for el in tripple:
        if el % 2 == 0 and len(str(abs(el))) == 4:
            f += 1
    if sum(tripple) <= m and f < 2:
        c += 1
        m_s = max(sum(tripple), m_s)
        print(tripple, sum(tripple), m)
print(c, m_s)
    