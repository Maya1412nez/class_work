def NOD(n, m, k):
    k1 = 0
    for i in range(1, min([n, m])):
        if n % i == 0 and m % i == 0:
            k1 = i
    return k1 == k

c = 0
for a in range(1, 1000):
    flag = 0
    for x in range(1, 1000):
        f = NOD(a, 420, 2) or (not(NOD(a, x, 12))) <= (not(NOD(110, x, 11)))
        if f == 0:
            flag = 1
    if flag == 0:
        c += 1
print(c)


    