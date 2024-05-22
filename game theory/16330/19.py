def f(a, b, h):
    if h > 2:
        return 0
    if a+b >= 59:
        return h == 2
    return any([f(a+1, b, h+1), f(a*2, b, h+1), f(a, b+1, h+1), f(a, b*2, h+1)])

for i in range(1, 54):
    if f(5, i, 0):
        print(i)

#14