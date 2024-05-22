s = 'ABCDEFGHIJKLMNOPQRSTUVW'
for i in range(22):
    if i > 9:
        letter = s[i-10]
    else:
        letter = str(i)
    if (int(f'98{letter}79641', 22) + int(f'36{letter}14', 22) + int(f'73{letter}4', 22)) % 21 == 0:
        print((int(f'98{letter}79641', 22) + int(f'36{letter}14', 22) + int(f'73{letter}4', 22)) / 21)