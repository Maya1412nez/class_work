row = open('8_june_ege/24_17563.txt').readline()

znaks = '*-'
nums = '0987'
c = 0
m_c = 0
l = []
s = ''
for i in range(len(row)):
    c += 1
    s += row[i]
    if row[i] in znaks and row[i+1] in znaks:
        m_c = max(c, m_c)
        c = 0
        l.append(s)
        s = ''

    if row[i] == '0' and row[i-1] in znaks:
        m_c = max(c, m_c)
        c = 0
        l.append(s)
        s = ''
l.sort(key=len)
print(l)
print(l[-1], len(l[-1]))
    

