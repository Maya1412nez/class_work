numbers = [x for x in range(-987656, 987656)]
c = 0
for i in range(123456, 987655):
    dels = []
    for j in range(2, i+1):
        if j != 0:
            if i % j == 0:
                c += 1
                dels.append(j)
            if c > 3:
                break
    if c == 3:
        print(dels)
        c = 0
