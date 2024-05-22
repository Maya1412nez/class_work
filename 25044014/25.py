numbers = [x for x in range(-987656, 987656)]
c = 0
for i in range(123456, 987655):
    dels = []
    for el in numbers:
        if el != 0:
            if i % el == 0:
                c += 1
                dels.append(el)
    if c == 5:
        dels1 = dels.copy()
        dels1.remove(max(dels))
        print(max(dels), max(dels1))
        c = 0
    if i % 1000 == 0:
        print(i)