def f(a, b, c, h):
    if h > 2:
        return 0
    if max([a, b, c]) >= 20 or a+b+c >= 25:
        return h == 2
    if h % 2 == 1:
        return any([f(a*2, b, c, h+1), f(a, b*2, c, h+1), f(a, b*2, c, h+1), f(a+2, b+2, c+2, h+1)])
    return all([f(a*2, b, c, h+1), f(a, b*2, c, h+1), f(a, b*2, c, h+1), f(a+2, b+2, c+2, h+1)])

def d(a, b, c, h):
    if h > 1:
        return 0
    if max([a, b, c]) >= 20 or a+b+c >= 25:
        return h == 1
    if h % 2 == 0:
        return any([d(a*2, b, c, h+1), d(a, b*2, c, h+1), d(a, b*2, c, h+1), d(a+2, b+2, c+2, h+1)])
    return all([d(a*2, b, c, h+1), d(a, b*2, c, h+1), d(a, b*2, c, h+1), d(a+2, b+2, c+2, h+1)])

for i in range(1, 20):
    if f(2, 3, i, 0) == 1 and d(2, 3, i, 0) == 0:
        print(i)