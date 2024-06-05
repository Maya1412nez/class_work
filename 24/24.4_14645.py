s = open('24/24.4_14645.txt').readline()

glas = 'EYUIOA'
sogl = 'QWRTPSDFGHJKLZXCVBNM'

c = 0
m = 0
rez_s = ''
m_rez_s = ''
for i in range(len(s) - 1):
    c += 1
    rez_s += s[i]
    if (s[i] in glas and s[i+1] in glas) or (s[i] in sogl and s[i+1] in sogl):
        m = max(m, c)
        c = 0
        # эта часть чист для проверки итоговой строки
        if len(m_rez_s) < len(rez_s):
            m_rez_s = rez_s + s[i+1]
        rez_s = s[i]

print(m_rez_s, len(m_rez_s), 'к итоговой строке дописываются стоящие рядом символы, все верно')
# часть закончилась
print(m)



