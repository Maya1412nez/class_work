def f(a, b, h):
    if h > 3:
        return 0
    if a+b >= 59:
        return h == 3
    if h % 2 == 0: # значит следующий ход - Петин
        return any([f(a+1, b, h+1), f(a*2, b, h+1), f(a, b+1, h+1), f(a, b*2, h+1)])
    return all([f(a+1, b, h+1), f(a*2, b, h+1), f(a, b+1, h+1), f(a, b*2, h+1)])


for i in range(1, 54):
    if f(5, i, 0):
        print(i)

# 24, 26