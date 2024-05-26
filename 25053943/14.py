letters = 'ABCDEFJH'
s = 0

for x in range(11):
    for y in range(11):
        x1, y1 = x, y
        if x > 9:
            x1 = letters[x - 10]
        if y > 9:
            y1 = letters[y - 10]
        f = int(f'{y1}23{x1}C', 14) + int(f'A{x1}910', 11)
        if f % 23 == 0:
            if int(str(x1), 11) + int(str(y1), 11) > s:
                chast = f / 23
                s =  int(str(x1), 11) + int(str(y1), 11)
print(chast)