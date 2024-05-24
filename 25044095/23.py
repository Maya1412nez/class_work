def f(n, rez, last):
    if n == rez and last != 'b':
        return 1
    if n > rez or (n == rez and last == 'b'):
        return 0
    return f(n+2, rez, 'a') + f(n+3, rez, 'b') + f(n*2, rez, 'c')

print(f(3, 20, ''))

