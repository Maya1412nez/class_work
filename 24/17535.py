s = open('24/17535.txt').readline()
# a = [1, 2, 3]
# b = a.copy()
# a.append(6)
# print(a, b)
s = s.replace('CD', 'C D')
l = s.split()
# print(l, len(l))
counter_CD = 0
len_max_s = 0
l1 = []
max_l = []
l_s = 0
for i in range(len(l)):
    l1.append(l[i])
    if counter_CD == 160:
        if len(''.join(l1)) > len(''.join(max_l)):
            max_l = l1.copy()
        l1.remove(l1[0])
        counter_CD -= 1

    counter_CD += 1
print(''.join(max_l), len(''.join(max_l)))

