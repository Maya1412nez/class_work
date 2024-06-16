def DEL(n, m):
    return n % m == 0
b = list(range(70, 91))
# print(b)

for a in range(1, 1000000):
    if all(( DEL(x, a) or ((x in b) <= (not(DEL(x, 22)))) ) for x in range(1, 500)):
        print(a)