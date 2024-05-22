def f(a, b, h):
    if h > 3:
        return 0
    if a+b >= 231:
        return h == 3
    if h % 2 == 0: # следующий - Петя
        return any([f(a+1, b, h+1), f(a, b+1, h+1), f(a*2, b, h+1), f(a, b*2, h+1)])
    return all([f(a+1, b, h+1), f(a, b+1, h+1), f(a*2, b, h+1), f(a, b*2, h+1)])

for s in range(1, 214):
    if f(17, s, 0):
        print(s)
