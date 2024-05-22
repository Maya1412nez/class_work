# import sys

# sys.setrecursionlimit(10 ** 6)

# def F(n):
#     if n < 11:
#         return 10
#     else:
#         return n + F(n - 1)
    
# # for n in range(2000):
# #     F(n)

# print(F(2124) - F(2122))

# l = ['A', 'B', 'C']
# c = 0
# f = 0
# m = 0
# f = open('24.txt')
# for row in f:
#     for letter in row:
#         if letter in l:
#             f += 1
#         else:
#             f = 0
#         if f == 2:
#             f = 0
#             if c > m:
#                 m = c
#             c = 0
#         else:
#             c += 1
# print(m)

c = 0
s = 0
f = 0
l_of_ses = []
sinl = []
f = open('24.txt')
for row in f:
    for letter1 in row:
        s += 1
        if letter1 == 'W':
            f += 1
        else:
            f = 0
        if f == 2:
            f = 0
            c += 1
            sinl.append(s)
            s = 0
        if c == 100:
            l_of_ses.append(sum(sinl))
            sinl.remove(sinl[0]) # 99
            c = 99
print(max(l_of_ses))
