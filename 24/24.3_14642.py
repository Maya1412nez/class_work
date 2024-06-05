import fnmatch

s = open('24/24.3_14642.txt'). readline()
m = 0

s = s.replace('F', 'F F')
l = s.split()
# els like 'F________F'
for i in range(len(l) - 1):
    # F____FF_______F
    m = max(len(l[i]+l[i+1]) - 3, m)

print(m)
