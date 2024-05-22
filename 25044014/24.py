f = open('25044014/24.txt')
for row in f:
    s = row
m = 0
c = 0
for i in range(len(s)):
    c += 1
    if s[i:i+4] == 'XZZY':
        m = max(c, m)
        c = 0
print(m)