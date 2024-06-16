def f(a, h):
    if h > 2:
        return 0
    if a >= 58:
        return h == 2
    if h % 2 == 1:
        return any([f(a+1, h + 1), f(a+4, h + 1), f(a*2, h + 1)])
    return all([f(a+1, h + 1), f(a+4, h + 1), f(a*2, h + 1)])

    

def d(a, h):
    if h > 1:
        return 0
    if a >= 58:
        return h == 1
    if h % 2 == 0:
        return any([d(a+1, h + 1), d(a+4, h + 1), d(a*2, h + 1)])
    return all([d(a+1, h + 1), d(a+4, h + 1), d(a*2, h + 1)])


for s in range(1, 58):
    if f(s, 0) and (not(d(s, 0))):
        print(s)