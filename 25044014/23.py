def f(n, rez):
    if n == rez:
        return 1
    if n > rez or n == 12:
        return 0
    return f(n+1, rez) + f(n+2, rez) + f(n * 2, rez)

print(f(2, 9) * f(9, 17))