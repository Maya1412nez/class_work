def ДЕЛ(x, y):
    return x % y == 0
for a in range(1, 1000):
    if all(((ДЕЛ(x, 15) and (not(ДЕЛ(x, 10)))) <= (a < x + 50)) for x in range(1000)):
        print(a)