import sys
sys.set_int_max_str_digits(10000)

number = 2 * 729 ** 2014 + 2 * 243 ** 2016 - 2 * 81 ** 2018 + 2 * 27 ** 2020  - 2 * 9 ** 2022 - 2024

def count_num_in_sis(n, sis):
    c = 0
    while n > 0:
        if n % sis > 9:
            c += 1
        n //= sis
    return c
# print(bin(45678)[2:])
# print(''.join(to_sis(45678, 2)))
print(count_num_in_sis(number, 27))
