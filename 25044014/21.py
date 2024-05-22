def f(a, b, h):
    if h > 4:
        return 0
    if a+b >= 231:
        return h in [2, 4]
    if h % 2 == 1: # следующий - Ваня   
        return any([f(a+1, b, h+1), f(a, b+1, h+1), f(a*2, b, h+1), f(a, b*2, h+1)])
    return all([f(a+1, b, h+1), f(a, b+1, h+1), f(a*2, b, h+1), f(a, b*2, h+1)])

def d(a, b, h):
    if h > 2:
        return 0
    if a+b >= 231:
        return h == 2
    return all([d(a+1, b, h+1), d(a, b+1, h+1), d(a*2, b, h+1), d(a, b*2, h+1)])



for s in range(1, 214):
    if f(17, s, 0) and d(17, s, 0) == 0:
        print(s)
