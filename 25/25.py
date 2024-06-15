

# print(f(4), f(13))
for i in range(800000, 1000000000):
    s = set()
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            s.add(j)
            s.add(i//j)
    l = sorted(list(s))
    # print(l)
    m = 0
    # if i == 800004:
    #     print(i, max(l) + min(l), l)
    if l:
        m = max(l) + min(l)
        if str(m)[-1] == '4':
            print(i, m)
            a = input()
    
