m = 0
for i in range(4, 10000):
    s = f'1{'9'*i}'
    while '19' in s or '49' in s or '999' in s:
        if '19' in s:
            s = s.replace('19', '9', 1)
        if '49' in s:
            s = s.replace('49', '91', 1)
        if '999' in s:
            s = s.replace('999', '4', 1)
    su = sum(list(map(int, list(s))))
    if su > m:
        m = su
print(m)