f = open('25044095/24_13866.txt')

for row in f:
    s = row
c = 0
m = 0
nums = '13579'
for i in range(len(row) - 2):
    c += 1
    if row[i] in nums and row[i+1] in nums and row[i+2] in nums:
        if m < c + 2:
            m = c + 1
        c = 0
print(m)