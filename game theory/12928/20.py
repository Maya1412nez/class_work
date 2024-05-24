def f(a, n):
    if n > 4:
        return 0
    if a >= 21:
        return n in [2, 4]
    if n % 2 == 1:
        return any([f(a+1, n+1), f(a*2, n+1)])
    return all([f(a+1, n+1), f(a*2, n+1)])


def d(a, n):
    if n > 2:
        return 0
    if a >= 21:
        return n in [2]
    if n % 2 == 1:
        return any([d(a+1, n+1), d(a*2, n+1)])
    return all([d(a+1, n+1), d(a*2, n+1)])

for i in range(1, 21):
    if f(i, 0) and d(i, 0) == 0:
        print(i)

# 8