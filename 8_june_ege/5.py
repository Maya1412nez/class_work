m_r = -100000000
for n in range(1, 13):
    n_b = bin(n)[2:]
    if n % 2 == 0:
        n1 = '10' + n_b
    else:
        n1 = '1' + n_b + '01'
    r = int(n1, 2)
    m_r = max(r, m_r)
    print(m_r)