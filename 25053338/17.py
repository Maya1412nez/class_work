f = open('25053338/17.txt')
l = []
max_sum = -1000000
mi = 10000000
counter = 0
for row in f:
    l.append(int(row))
    if int(row) % 19 == 0:
        mi = min(mi, int(row))

for i in range(len(l) - 1):
    couple = [l[i], l[i+1]]
    if couple[0] % mi == 0 or couple[1] % mi == 0:
        counter += 1
        max_sum = max(max_sum, sum(couple))
        print(couple, couple[0] % mi, couple[1] % mi)
print(counter, max_sum)
        
        