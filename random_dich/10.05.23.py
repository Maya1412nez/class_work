file = open('13.txt')
data = file.read().splitlines()
lst = list(map(int, data))
c = 0
for i in range(len(lst) - 1):
    if lst[i] % 8 == 0 and lst[i + 1] % 8 == 0:
        c += 1

print(c)