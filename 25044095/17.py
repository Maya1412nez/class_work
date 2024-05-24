f = open('25044095/17_13858.txt')
l = []
mi = 100000000
for row in f:
    l.append(int(row))
    if int(row) < mi and str(abs(int(row)))[-2:] == '25':
        mi = int(row)
print(mi)
import time
time.sleep(2)
c = 0
ma = 0
for i in range(len(l) - 2):
    tripple = [l[i], l[i+1], l[i+2]]
    c_4 = 0
    proiz = 1
    for el in tripple:
        if len(str(abs(el))) == 4:
            c_4 += 1
            proiz *= el
    if proiz <= (mi ** 2):
        if c_4 > 1:
            c += 1
            if proiz > ma:
                ma = proiz
print(c, ma, mi ** 2)