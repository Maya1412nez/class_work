def f(a, b, h):
    if h > 2:
        return 0
    if a+b <= 36:
        return h == 2
    if h % 2 == 1:
        return any([f(a - 3, b, h+1), f(a // 2 + (a%2), b, h+1), f(a, b - 3, h+1), f(a, b // 2 + (b%2), h+1)])
    return all([f(a - 3, b, h+1), f(a // 2 + (a%2), b, h+1), f(a, b - 3, h+1), f(a, b // 2 + (b%2), h+1)])

for i in range(17, 100):
    if f(20, i, 0):
        print(i)
