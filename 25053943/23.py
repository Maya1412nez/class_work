def f(n, rez):
    if n == rez:
        return 1
    if n > rez or n == 11:
        return 0
    if (n % 3 == 0):
        k = 0
    else:
        k = f(n + (n % 3), rez)
    return f(n + 1, rez) + f(n * 2, rez) + k

print(f(3, 18))