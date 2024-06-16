import fnmatch

for i in range(10**8):
    if fnmatch.fnmatch(str(i), '1*03*6*'):
        if i % 22768 == 0:
            print(i)