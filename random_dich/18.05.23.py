# a = '125 101 115 114 101 118 110 105 123 89 69 75'
# for el in a.split():
#     pass
# def f(n):
#     if n <= 2:
#         return 1
#     return n + f(n - 3) + f(n - 42)
# for i in range(2100):
#     f(i)
# print(f(3) + f(20))
# print(1)
# print((f(2023) + f(2021) - 2 * f(213)))
# print(2)

# lst = [1, 2, 3]
# it_lst = iter(lst)
# while True:
#     print(next(it_lst))
#     if next(it_lst) == lst[-1]:
#         print(lst[-1])
#         break


# 19.05.2023

# lst = [1, 5, 6, 2]
# lst_it = iter(lst)
# while x := next(lst_it, None):
#     print(x)


def own_range(start, end, step):
    if start > end:
        i = end
        while i > end:
        # print(start, i, end)
            i += step
            yield i - 1
    else:
        i = start
        while i < end:
            # print(start, i, end)
            i += step
            yield i - 1

for i in own_range(4, 1, -1):
    print(i)


class Koshelek:
    def __init__(self, denygi=None):
        self.denygi = [-122, 80, -1000]
        self.i = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        self.i += 1
        if self.i > len(self.denygi):
            raise StopIteration
        return self.denygi[self.i - 1]

class Counter:
    def __init__(self, n) -> None:
        self.i = 0
        self.n = n

    def __iter__(self):
        return self
    
    def __next__(self):
        self.i += 1
        if self.i > self.n:
            raise StopIteration
        return self.i - 1
    
