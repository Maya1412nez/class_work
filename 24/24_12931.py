s = open('24/24_12931.txt').readline()

c = 0
for i in range(1000):
    if i * 'VWXYZ' in s:
        c = i
s = s.replace(c*'VWXYZ', ' ')
l = s.split()
print(l[0][-5:], l[1][:5], len(c*'VWXYZ'))
print(len(c*'VWXYZ') + 3 + 2)