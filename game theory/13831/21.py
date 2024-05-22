def f(a, h):
    if h > 4 :
        return 0
    if a >= 512:
        return h in [2, 4]
    if h % 2 == 1:# Следующий - Ваня
        return any([f(a+2, h+1), f(a+3, h+1), f(a+4, h+1), f(a+5, h+1), f(a*2, h+1)])
    return all([f(a+2, h+1), f(a+3, h+1), f(a+4, h+1), f(a+5, h+1), f(a*2, h+1)])

def d(a, h):
    if h > 2:
        return 0
    if a >= 512:
        return h == 2
    return all([d(a+2, h+1), d(a+3, h+1), d(a+4, h+1), d(a+5, h+1), d(a*2, h+1)])


for i in range(1, 512):
    if f(i, 0) == 1 and d(i, 0) == 0:
        print(i)

# 247, но их много, хотя просят одно :О