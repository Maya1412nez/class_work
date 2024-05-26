for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = (y <= (w == z)) or (not(x <= z))
                if f == 0:
                    print(z, y, w, x)