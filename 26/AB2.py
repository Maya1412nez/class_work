f = open('26/26.2.txt')
l = []
for row in f:
    r = list(map(int, row.split()))
    l.append(r)
l.sort()
# print(l, len(l))
first = []
second = []
# for row in l:
#     if row[-1] == 1:
#         first

# a = [0, 0, 1, 2, 3]
# a.remove(a[0])
# print(a)

time = 0
queue1 = []
queue2 = []
count_1 = 0
count_2 = 0
ushlo = 0
all_clients_1 = 0
for time in range(10000):
    for row in l:
        if row[0] == time:
            if row[-1] == 1: # Если нужна именно 1 очередь
                if count_1 < 12: # Если в очереди менее 12 чел
                    queue1.append(row[1])
                    count_1 += 1
                    all_clients_1 += 1
                else:
                    ushlo += 1
            elif row[-1] == 2: # Если нужна именно 2 очередь
                if count_2 < 12: # Если в очереди менее 12 чел
                    queue2.append(row[1])
                    count_2 += 1
                else:
                    ushlo += 1
            elif row[-1] == 0: # Любая очередь
                if count_1 <= count_2: # Вычисление оптимальной очереди
                    if count_1 < 12:# Если в очереди менее 12 чел
                        queue1.append(row[1])
                        count_1 += 1
                        all_clients_1 += 1
                    else:
                        ushlo += 1
                else:
                    if count_2 < 12: # Если в очереди менее 12 чел
                        queue2.append(row[1])
                        count_2 += 1
                    else:
                        ushlo += 1

        # Симуляция течения времени
        if len(queue1) > 0:
            if queue1[0] > 0:
                queue1[0] -= 1
            else:
                queue1.remove(queue1[0])
        
        if len(queue2) > 0:
            if queue2[0] > 0:
                queue2[0] -= 1
            else:
                queue2.remove(queue2[0])

                    
print(all_clients_1, ushlo)
            