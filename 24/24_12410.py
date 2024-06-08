s = open('24/24_12410.txt').readline()

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# c = 0
# c1 = 0
# to_replace = ''
# for letter in s:
#     if letter == alphabet[c]:
#         c += 1
#     else:
#         c = 0
#         to_replace += letter
#     if c1 % 10000 == 0:
#         print(c1, len(s), c1 < len(s))
#     c1 += 1
# print(len(to_replace))
# for i in range(len(to_replace)):
#     s = s.replace(to_replace[i], to_replace[i]+' '+to_replace[i], 1)
# l = s.split()
# print(l, len(l))
    
for i in range(26, 0, -1):
    s = s.replace(alphabet[:i], f'{i} {i}')
l = s.split()
print(l, len(l))