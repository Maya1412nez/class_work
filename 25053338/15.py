def DEL(n, m):
    return n % m == 0

for a in range(1, 100000):
    if all(((not(DEL(x, a))) <= ((DEL(x, 14)) <= (not(DEL(x, 4))))) for x in range(1000)):
        print(a)

# for a in range(1,1000):
#     for x in range(500):
#         f = (not(DEL(x, a))) <= ((DEL(x, 14)) <= (not(DEL(x, 4))))
#         if 