for n in range(1, 1000):
    n_bin = bin(n)[2:]
    if n % 2 == 0:
        n1 = '10' + n_bin
    else:
        n1 = '1' + n_bin + '01'
    r = int(n1, 2)
    if r > 516:
        print(n)
        break
