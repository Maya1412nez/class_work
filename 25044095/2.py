for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = ((not(x)) and (z <= y) and (not(w))) or ((z == w) and (x or y <= w))
                if f and y == 1:
                    print(x, y, z, w, f)