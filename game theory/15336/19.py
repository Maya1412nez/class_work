def f(a, b, h):
    if h > 2:
        return 0
    if a + b >= 123:
        return h == 2
    return f(a+1, b, h+1) or f(a*2, b, h+1) or f(a, b+1, h+1) or f(a, b*2, h+1)

for i in range(1, 110):
    if f(13, i, 0):
        print(i)
        break

# 28