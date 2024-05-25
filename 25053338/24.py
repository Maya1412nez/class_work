f = open('25053338/24.txt')

LETTERS = 'QRW'
NUMBERS = '124'

def first(s):
    c = 0
    m_c = 0
    for i in range(len(s) - 1):
        # print(s[i], s[i+1], (s[i] in LETTERS and s[i+1] in LETTERS) or (s[i] in NUMBERS and s[i+1] in NUMBERS))
        if (s[i] in LETTERS and s[i+1] in LETTERS) or (s[i] in NUMBERS and s[i+1] in NUMBERS):
            m_c = max(m_c, c)
            c = 0
        c += 1
    m_c = max(m_c, c)
    print(m_c)
    return None

# 2
import itertools

def second(s):
    for comb in itertools.product(LETTERS, repeat=2):
        s = s.replace(''.join(comb), ' ')

    for comb in itertools.product(NUMBERS, repeat=2):
        s = s.replace(''.join(comb), ' ')

    s1 = s.split()
    lens = []
    for el in s1:
        lens.append(len(el) + 2)

    print(max(lens))
    return None


''' это решение не проканает, если будут идти подряд 3 буквы или цифры:
Пример:
    "QQQ1Q2Q44"
программа удалит "QQ" и "44", оставив "Q1Q2Q". 
Но в этом случае мы не можем спокойно прибавить 2 (добавляя по символу справа и слева),
тк тогда мы получим строку "QQ1Q2Q4", в которой 2 буквы идут подряд

'''

# MAIN
for row in f:
    s = row

first(s)
second(s)

# Проверка алгоритмов

st = "QQQ1Q2Q44"
first(st)
second(st)
