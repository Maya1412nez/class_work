import fnmatch


for i in range(1353, 10**9, 1353):
    if str(i).count('1') == 4:
        if fnmatch.fnmatch(str(i), '1?3*4?*9'):
            print(i, i//1353)
