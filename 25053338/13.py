def b(n, razr=8):
    return '0' * (razr - len(bin(n)[2:])) + bin(n)[2:]

c = 0
part_of_net = f'{b(122)}.{b(159)}.{b(136)}.10010'
for i in range(2**3):
    net = part_of_net + b(i, razr=3)
    if net.count('1') % 4 != 0:
        c += 1
        print(net, net.count('1'))
print(c)