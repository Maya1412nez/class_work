def f(a, b, h):
    if h > 4:
        return 0
    if a+b >= 59:
        return h == 2 or h == 4
    if h % 2 == 1: # следующий ход - Ванин (а сейчас Петя)
        return any([f(a+1, b, h+1), f(a*2, b, h+1), f(a, b+1, h+1), f(a, b*2, h+1)])
    return all([f(a+1, b, h+1), f(a*2, b, h+1), f(a, b+1, h+1), f(a, b*2, h+1)])

def d(a, b, h):
    if h > 2:
        return 0
    if a+b >= 59:
        return h == 2
    return all([d(a+1, b, h+1), d(a*2, b, h+1), d(a, b+1, h+1), d(a, b*2, h+1)])

for i in range(1, 54):
    if f(5, i, 0) and (not(d(5, i, 0))):
        print(i)

# 23

