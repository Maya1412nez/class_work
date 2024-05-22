import itertools


counter = 0
for comb in itertools.product('01234567', repeat=5):
    if comb[0] != 0:
        c = 1
        f = 0
        m_c = 0
        for i in range(len(comb) - 1):
            if comb[i] == comb[i+1]:
                c += 1
            else:
                c = 1
            m_c = max(c, m_c)
        if len(set(comb)) == 3:
            f = 1
        if f == 1 and m_c == 3:
            # print(comb, f, m_c)
            counter += 1


print(counter)


            
