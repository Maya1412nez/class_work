f = open('17/17_13882.txt')
 
l = []
m = 0
c = 0
for row in f:
    l.append(int(row))
    if int(row) % 401 == 0:
        m = max(m, int(row))
# print(m, m / 401)

mi = 99999999999999999999999
for i in range(len(l) - 2):
    sums = set()
    trip = l[i:i+3]
    # print(trip)
    for el in trip:
        sums.add(sum((list(map(int, list(map(int, list(str(el)))))))))
        # print(el, (list(map(int, list(map(int, list(str(el))))))))
    if len(sums) == 3:
        if sum(trip) > m:
            c += 1
            print(trip, sums)
            mi = min(sum(trip), mi)
print(c, mi)