def b(n, razr=8):
    return '0' * (razr - len(bin(n)[2:])) + bin(n)[2:]
# print(b(123))
part_of_net1 = f'{b(199)}.{b(29)}.'
part_of_part_of_net2 = f'{b(200)}.'

c = 0
for i in range(256):
    part_of_net2 = part_of_part_of_net2 + b(i)
    if part_of_net1.count('1') < part_of_net2.count('1'):
        c += 1
    # print(part_of_net1, part_of_net2, part_of_net1.count('1'), part_of_net2.count('1'))

print(c)