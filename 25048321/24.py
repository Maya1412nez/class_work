f = open('25048321/24.txt')

for row in f:
    s = str(row)

c = 0
f = 0
m_c = 0
m_s1 = 0
s1 = ''
for i in range(len(s) // 3):
    word = s[i] + s[i+1] + s[i+2]
    if (word == 'NPO' or word == 'PON') and (f == 0 or f == 3):
        f = 1
        c += 1
        s1 += word
    elif f > 0 and f < 3:
        f += 1
    else:
        f = 0
        c = 0
        s1 = ''
    if c > m_c:
        m_c = c
        m_s1 = s1
print(m_c)
print(m_s1)
