a = 'ABCDEFGHIJKL'

for x in range(18):
    x1 = x
    if x > 9:
        x1 = a[x-10]
    f = int(f'71{x1}264', 18) + int(f'4{x1}51{x1}1', 18) + int(f'21{x1}637', 18)
    if f % 17 == 0:
        print(f / 17, x)