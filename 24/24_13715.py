import fnmatch

s = open('24/24_13715.txt').readline()

s = s.replace('AB', ' ')
l = s.split()
# print(l)
# ABEABDCDABEDABEABCABEDABEEABDABCABD
#   E  DCD  ED  E  C  ED  EE  D  C  D
m = 0
for i in range(len(l)):
    group = l[i:i+50]
    # print(len(group))
    m = max(m, len(''.join(group)) + 100)
print(m)

# да в пень