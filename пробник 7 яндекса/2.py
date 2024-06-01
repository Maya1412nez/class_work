for x in range(2):
    for y in range(2):
        for u in range(2):
            for w in range(2):
                f = (not((y <= w) == x)) and u
                if sum([x, y, u, w]) == 3 and f == 0:
                    print(x, y, u, w, f)