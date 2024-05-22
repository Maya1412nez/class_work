def f(a, h):
    if h > 4:
        return 0
    if a >= 84:
        return h in [2, 4]
    if h % 2 == 1:
        if a % 2 == 0:
            return any([f(a+1, h+1), f(a * 1.5, h+1)])
        return any([f(a+1, h+1), f(a * 2, h+1)])
    if a % 2 == 0:
        return all([f(a+1, h+1), f(a * 1.5, h+1)])
    return all([f(a+1, h+1), f(a * 2, h+1)])

def d(a, h):
    if h > 2:
        return 0
    if a >= 84:
        return h == 2
    if a % 2 == 0:
        return all([d(a+1, h+1), d(a * 1.5, h+1)])
    return all([d(a+1, h+1), d(a * 2, h+1)])

for i in range(1, 84):
    if f(i, 0) == 1 and d(i, 0) == 0:
        print(i)

# 54