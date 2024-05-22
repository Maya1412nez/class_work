for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                f = (x or ((not(z)) and w) or w) == (y and (not(x)) and w)
                if f == 1 and sum([x, y, z, w]) > 0:
                    print(x, y, z, w, f)