f = open('8_june_ege/17_17558.txt')
l = []
c_32 = 0

for row in f:
    l.append(int(row))
    if int(row) % 32 == 0:
        c_32 += 1

# print(l, len(l), c_32)
c = 0
m_s = -1000000000
for i in range(len(l) - 1):
    couple = l[i:i+2]
    # print(couple)
    usl_1 = 0
    usl_2 = 0
    for el in couple:
        if el < 0:
            usl_1 = 1
    if sum(couple) < c_32:
        usl_2 = 1
    if usl_1 and usl_2:
        c += 1
        print(couple)
        m_s = max(sum(couple), m_s)
print(c, m_s)
