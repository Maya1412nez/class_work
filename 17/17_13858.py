f = open('17/17_13858.txt')

l = []
mi = 9999999999999999999999
for row in f:
    l.append(int(row))
    if str(int(row))[-2:] == '25':
        mi = min(mi, int(row))
    # print(str(int(row))[-2:], mi)

c = 0
m_p = 0
for i in range(len(l) - 2):
    trip = l[i:i+3]
    # print(trip)
    f1 = 0
    proiz = 1
    for el in trip:
        if len(str(abs(el))) == 4:
            f1 += 1
        proiz *= el
    if f1 >= 2 and proiz <= mi ** 2:
        c += 1
        print(trip, proiz, mi**2)
        m_p = max(proiz, m_p)

print(c, m_p)   