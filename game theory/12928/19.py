def f(a, n):
    if n > 3:
        return 0
    if a >= 21:
        return n == 3
    if n % 2 == 0:
        return any([f(a+1, n+1), f(a*2, n+1)])
    return all([f(a+1, n+1), f(a*2, n+1)])

for i in range(1, 21):
    if f(i, 0):
        print(i)

# 5