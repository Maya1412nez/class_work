for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = (not(x <= z)) or (y == w) or y
                f1 = (x > z) or (y == w) or y
                if f == 0:
                    print(z, x, y, w)
