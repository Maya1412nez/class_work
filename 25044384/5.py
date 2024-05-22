def to_sis(n, sis):
    a = ''
    while n > 0:
        a += str(n % sis)
        n //= sis
    return a[::-1]

m = 0
for n in range(1, 10000):
    n1 = to_sis(n, 4)
    if n % 3 == 0:
        n2 = n1[-1] + n1[1:-1] + n1[0] + '1'
    else:
        n2 = n1 + str(n % 3)
    r = int(n2, 4)
    if r <= 340 and r > m:
        m = r
print(m)