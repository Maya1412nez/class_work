s = open('24/24.3_14646.txt').readline()

letters = 'QWERTYUIOPASDFGHJKLZXCVBNM'

for let in letters:
    # print(let*3)
    while let*3 in s:
        s = s.replace(let*3, ' ')

# l = s.split()
d = dict()
for let in letters:
    d[let[0]] = s.count(' '+let)
# print(d)
for key, val in d.items():
    if val == max(d.values()):
        print(key+str(val))
print('Ответ 1: L65', '(неправильный)', '\n')
# print('K', d.keys(), 'F' in d.keys())


# ------------------2 метод----------------

import fnmatch
d1 = dict()
s = open('24/24.3_14646.txt').readline()
for i in range(len(s) - 3):
    quartet = s[i:i+4]
    for let in letters:
        if fnmatch.fnmatch(quartet, f'{let*3}?'):
            if quartet[-1] not in d1.keys():
                d1[quartet[-1]] = 0
            d1[quartet[-1]] += 1

for key, val in d1.items():
    if val == max(d1.values()):
        print(key+str(val))
# print(d1)
print('Ответ 2: T69 (правильный)', '\n')


print('''
Примерная строка - GGGGH

Ответы могут отличаться, тк в первом случае мы удаляем тройки (в случае с прим. стр. - удаляем GGG), в результате
засчитывая только четвертую букву G (как, собственно, в примере показано, но ладно. Будем считать, они вывели не все случаи)

Во втором же решении мы считаем сначала GGG+G, засчитав 1 для буквы G, а потом считываем еще и GGGH, засчитывая 1 для H, 
чего не делается в первом случае

Вывод 1: потоковое считывание надежнее)))) (когда работает)
Вывод 2: не смотрите пж задачи от слова пацана
''')