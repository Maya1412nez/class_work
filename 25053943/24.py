f = open('25053943/2024_var3_ege24_16455.txt')

for row in f:
    s = row
c = 0
m = 0
abc = 'ABC'
nums = '123'
for i in range(len(s) - 1):
    if (s[i] in abc and s[i+1] in abc) or (s[i] in nums and s[i+1] in nums):
        m = max(c, m)
        c = 0
    c += 1
print(m)
# ab1a2a33