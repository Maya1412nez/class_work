# s = '12312'
# s = s.replace('1', '00', 1)
# print(s)

for n in range(4, 10000):
    s = f'5{n * '2'}'
    su = 0
    while '72' in s or '522' in s or '2222' in s:
        if '72' in s:
            s = s.replace('72', '2', 1)
        if '522' in s:
            s = s.replace('522', '27')
        if '2222' in s:
            s = s.replace('2222', '5')
    for el in s:
        su += int(el)
    if su == 22:
        print(n, s)