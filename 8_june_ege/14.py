def to_sis(n, sis):
    a = ''
    while n > 0:
        a += str(n % sis)
        n //= sis
    return a[::-1]
# print(bin(12345678)[2:])
# print(to_sis(12345678, 2)[:])

ans = 0
for x in range(1, 2031):
    f = 7 ** 91 + 7 ** 160 - x
    f1 = to_sis(f, 7)
    if f1.count('0') == 70:
        ans = x
    print(f1, x, ans)
print(ans)