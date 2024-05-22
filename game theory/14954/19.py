def f(a, b, c, h):
    if h > 2 or (h == 1 and (max([a, b, c]) >= 20 or a+b+c >= 25)):
        return 0
    if max([a, b, c]) >= 20 or a+b+c >= 25:
        return h == 2
    if h % 2 == 0: # Следующих ход - Петин
        return any([f(a*2, b, c, h+1), f(a, b*2, c, h+1), f(a, b, c * 2, h+1), f(a+2, b+2, c+2, h+1)]) # Петя
    return all([f(a*2, b, c, h+1), f(a, b*2, c, h+1), f(a, b, c*2, h+1), f(a+2, b+2, c+2, h+1)]) # Ваня

for i in range(1, 20):
    if f(2, 3, i, 0):
        print(i)