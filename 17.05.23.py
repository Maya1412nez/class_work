def own_range(start, end, step):
    i = min(start, end) + (int(bool(step)))
    while start != i and i != end:
        print(start, i, end)
        i += step
        yield i

for i in own_range(5, 1, 1):
    print(i)
    if i > 100:
        break

# def r(n):
#     return [i for i in range(n)]

# for i in r(9999999999999999999999999999999999999):
#     print(i)