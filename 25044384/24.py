f = open('25044384/24.txt')
for row in f:
    s = row

c = 0
for i in range(len(s)):
    if s[i] == '1' or s[i] == '2':
        j = 0
        while s[i + j] in ['0', '1', '2']:
            c += 1
            j += 1
    if i % 10 == 0:
        print(100 / len(s) * i)
print(c)