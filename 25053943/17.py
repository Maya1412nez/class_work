f = open('25053943/2024_var3_ege17_16450.txt')
l = []

for row in f:
    l.append(int(row))

# def to_sis(n, sis):
#     a = ''
#     while n > 0:
#         a += str(n % sis)
#         n //= sis
#     return a[::-1]
c = 0
mi = 10000000000
for i in range(len(l) - 2):
    tripple = [l[i], l[i+1], l[i+2]]
    f = 0
    f1 = 0
    for el in tripple:
        s = 0
        for letter in str(el):
            s += int(letter)
        if s % 2 == 0:
            f = 1   
        # if to_sis(el, 6)[-1] == '3':
        if el % 6 == 3:
            f1 = 1
    if f == 0 and f1 == 1:
        c += 1
        mi = min(min(tripple), mi)
        # print(tripple, f, f1)
print(c, mi)