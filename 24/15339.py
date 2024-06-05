s = open('24/15339.txt').readline()
s1 = open('24/15339.txt').readline()

letters = 'ABC'
nums = '6789'
c = 0
m = 0
for i in range(len(s) - 1):
    c += 1
    if (s[i] in letters and s[i+1] in letters) or (s[i] in nums and s[i+1] in nums):
        m = max(c, m)
        c = 0
print(m)

# for let in letters:
#     for num in nums:
#         couple1 = let + num
#         couple2 = num + let
#         s1 = s1.replace(couple1, let + ' ' + num)
#         s1 = s1.replace(couple2, num + ' ' + let)
# print(s1.split())
# print(max(list(map(len, s1.split()))))


letters = 'BC'
nums = '789'

for let in letters:
    s1 = s1.replace(let, 'A')

for num in nums:
    s1 = s1.replace(num, '6')

while 'AA' in s1 or '66' in s1:
    s1 = s1.replace('AA', 'A A').replace('66', '6 6')

print(s1.split())

print(max(list(map(len, s1.split()))))