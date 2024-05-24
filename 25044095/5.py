def to_sis(n, sis):
    a = ''
    while n > 0:
        a += str(n % sis)
        n //= sis
    return a[::-1]

# print(to_sis(2345678, 2))
# print(bin(2345678)[2:])

mi = 100000

for n in range(1, 1000):
    n3 = to_sis(n, 3)
    if n % 7 == 0:
        n1 = n3 + n3[-2:]
        # print(n3[-2:])
    else:
        ost = to_sis((n % 7) * 3, 3)
        n1 = n3 + ost
    r = int(n1, 3)
    if r < mi and r > 369:
        mi = r
print(mi)
    