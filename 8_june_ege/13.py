def d(n, razr=8):
    return '0' * (razr - len(bin(n)[2:])) + bin(n)[2:]

part_of_net = f'{d(112)}.1010'

c = 0
for i in range(2 ** 20):
    net = part_of_net + d(i, razr=20)
    if net.count('1') % 3 != 0:
    # print(net)
        c += 1
    # a = input()
print(c)