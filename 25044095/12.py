
for n in range(4, 10000):
    s = '5' + n * '2'
    while '72' in s or '522' in s or '2222' in s:
        if '72' in s:
            s = s.replace('72', '2', 1)
        elif '522' in s:
            s = s.replace('522', '27', 1)
        else:
            s = s.replace('2222', '5', 1)
    if sum(list(map(int, list(s)))) == 22:
        print(s)
        print(n)
        break
    if len(str(sum(list(map(int, list(s)))))) > 1:
        print(s, (s, sum(list(map(int, list(s))))))
    if n % 100 == 0:
        print(f'{n // 100}% done')
        
