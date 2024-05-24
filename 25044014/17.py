f = open('25044014/17.txt')
l = []
m = -10000000
for row in f:
    l.append(int(row))
    # print(int(row), str(int(row))[-3:], '221', row[-3:] == '221')
    if int(row) > m and str(int(row))[-3:] == '221':
        m = int(row)
print(m)
# import time
# time.sleep(3)
counter = 0
mi = 10000000
for i in range(len(l) - 2):
    tripple = [l[i], l[i+1], l[i+2]]
    c, c2 = 0, 0
    for el in tripple:
        if len(str(abs(el))) > 1 and int(str(abs(el))[-2]) % 2 == 1:
            c += 1
        if len(str(abs(el))) == 2:
            c2 += 1
    # print(tripple, c, c2, sum(tripple))
    if c == 2 and c2 <= 2 and sum(tripple) > m:
        counter += 1
        # print(tripple)
    if sum(tripple) < mi:
        mi = sum(tripple)
print(counter, mi)
        