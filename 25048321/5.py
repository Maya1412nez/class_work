def to_sis(n, sis):
    a = ''
    while n > 0:
        a+= str(n%sis)
        n //=sis
    return a[::-1]

m = 100000

for n in range(1, 1000):
    n1 = to_sis(n, 3)
    if n % 3 == 0:
        n2 = n1 + n1[-2:]
    else:
        n_ost = n % 3
        n_ost2 = to_sis(n_ost*5, 3)
        n2 = n1 + n_ost2
    r = int(n2, 3)
    if r > 133 and r < m:
        m = r
print(m)