for n in range(1000, 0, -1):
    if int(f'1{sum(list(map(int, list(bin(n)[2:])))) % 2}' + (bin(n)[2:] + str(sum(list(map(int, list(bin(n)[2:])))) % 2))[2:], 2) < 35:
        print(n)
        break



# for n in range(1000, 0, -1):
#     n_bin = bin(n)[2:]
#     if sum(list(map(int, list(n_bin)))) % 2 == 0:
#         n1 = n_bin + '0'
#         n1 = '10' + n1[2:]
#     else:
#         n1 = n_bin + '1'
#         n1 = '11' + n1[2:]
#     r = int(n1, 2)
#     if r < 35:
#         print(n)
#         break
