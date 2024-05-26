def f(a, b, h):
    if h > 3:
        return 0
    if a + b >= 226:
        return h == 3
    if h % 2 == 0:
        return any([f(a+2, b, h+1), f(a, b+2, h+1), f(a*3, b, h+1), f(a, b*3, h+1)])
    return all([f(a+2, b, h+1), f(a, b+2, h+1), f(a*3, b, h+1), f(a, b*3, h+1)])


def d(a, b, h):
    if h > 1:
        return 0
    if a+b >= 226:
        return h == 1
    if h % 2 == 0:
        return any([d(a+2, b, h+1), d(a, b+2, h+1), d(a*3, b, h+1), d(a, b*3, h+1)])
    return all([d(a+2, b, h+1), d(a, b+2, h+1), d(a*3, b, h+1), d(a, b*3, h+1)])


for s in range(1, 209):
    if f(16, s, 0) and d(16, s, 0) == 0:
        print(s)
