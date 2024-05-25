import fnmatch

for i in range(1917, 10**10, 1917):
    if fnmatch.fnmatch(str(i), '3?12?14*5'):
        print(i, i // 1917)