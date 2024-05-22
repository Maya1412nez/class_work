def f(n, rez):
    if n == rez:
        return 1
    if n < rez:
        return 0
    return f(n-1, rez) + f(n // 2, rez)

print(f(30, 12) * f(12, 1))