for a in range(1, 1000):
    if all((x & 45 != 0) <= (x & a != 0) or (not((x & 19 != 0) or (x & a != 0))) for x in range(1, 1000)):
        print(a)
        break