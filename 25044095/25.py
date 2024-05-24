mask = 'ЧNЧЧNЧN77'
chet = '02468'
nechet = '13579'
for i in range(10 ** 7, 10 ** 9):
    s = str(i)
    if len(s) < len(mask):
        s = '0' + s
    if s[0] in chet and s[2] in chet and s[3] in chet and s[5] in chet:
        if s[1] in nechet and s[4] in nechet and s[6]:
            if s[-2:] == '77':
                if i % 7777 == 0:
                    print(s, i // 7777)
                
    