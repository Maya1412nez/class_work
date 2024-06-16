for i in range(700000, 1000000000):
    dels = set()
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            dels.add(j)
            dels.add(i//j)
    if dels:
        m = max(list(dels)) + min(list(dels))
        if m % 10 == 4:
            print(i, m)
            a = input()

