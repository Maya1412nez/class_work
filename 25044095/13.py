import ipaddress

def to_bin(n, razr=8):
    return '0' * (razr - len(bin(n)[2:])) + bin(n)[2:]
c = 0
mask = 26
net = to_bin(192) + '.' + to_bin(168) + '.' + to_bin(32) + '.' + '00'
for i in range(64):
    part = to_bin(i, razr=6)
    net1 = net + part
    if net1.count('1') % 5 != 0:
        print(net1, i)
        c += 1
print(c)