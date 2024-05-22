f = open('25048321/17.txt', 'r')
f1 = []
m = -100000
for row in f.readlines():
    f1.append(int(row))
    if row[-3:] == '121' and int(row) > m:
        m = int(row)

        print(m)

c = 0
m_s = -1000000
for i in range(len(f1) - 2):
    tripple = [f1[i], f1[i+1], f1[i+2]]
    chet = 0
    for el in tripple:
        if len(str(abs(el))) == 4 and abs(el) % 2 == 0:
            chet += 1
    if sum(tripple) <= m and chet < 2:
        c += 1
        if sum(tripple) > m_s:
            m_s = sum(tripple)
        # print(tripple, len(str(abs(f1[i]))), len(str(abs(f1[i + 1]))), len(str(abs(f1[i + 2]))), f1[i] % 2, f1[i+1] % 2, f1[i+2] % 2, chet)

print(c, m_s)