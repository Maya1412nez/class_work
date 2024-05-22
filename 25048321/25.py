from fnmatch import *

c = 0
for i in range(680000):
    if fnmatch(str(i), '1*2*'):
        if i % 8 == 0:
            c += 1
            # print(i)
print(c)