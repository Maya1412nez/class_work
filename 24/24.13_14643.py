# 1

s = open('24/24.13_14643.txt').readline()

while 'AXMM' in s:
    s = s.replace('AXMM', 'AXM XMM')

l = s.split()
print(max(list(map(len, l))))


# 2

s = open('24/24.13_14643.txt').readline()
c = 0
m = 0
for i in range(len(s) - 3):
    c += 1
    quartet = s[i:i+4]
    if quartet == 'AXMM':
        c += 2
        m = max(m, c)
        c = 0
print(m)

# С первой попытки в обоих случаях В]