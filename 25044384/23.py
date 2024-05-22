def f(n, rez):
    if n == rez:
        return 1
    if n > rez or n == 20:
        return 0
    return f(n+1, rez) + f(n+3, rez) + f(n**2, rez)
print(f(3, 23) + f(23, 25))    