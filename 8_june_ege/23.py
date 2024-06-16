def f(n, rez):
    if n == rez:
        return 1
    if n > rez:
        return 0
    return f(n + 1, rez) + f(n+2, rez) + f(n+3, rez)

print(f(5, 7) * f(7, 11))