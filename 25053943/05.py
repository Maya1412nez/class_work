def invert(n):
    rez = ''
    for el in n:
        rez += str(int(not(int(el))))
        # print(el, str(int(not(int(el)))))
    return rez

# print(bin(2345678)[2:])
# print(invert(bin(2345678)[2:]))
mi = 1000000
for n in range(1000):
    n_bin = bin(n)[2:]
    n1 = invert(n_bin)
    n2 = n1 + f'1{n % 2}'
    r = int(n2, 2)
    if r > 125:
        mi = min(r, mi)
    # print(n, n_bin, n1, n2, r)
    
print(mi)