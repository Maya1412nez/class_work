l = 'ABCDEFGHIJKLMNOP'
for x in range(17, 0, -1):
    x1 = x
    if x > 9:
        x1 = l[x-10]
    if int(f'71{x1}264', 18) + int(f'4{x}51{x}1', 18) + int(f'21{x}637', 18) % 17 == 0:
        print(int(f'71{x1}264', 18) + int(f'4{x}51{x}1', 18) + int(f'21{x}637', 18) / 17)