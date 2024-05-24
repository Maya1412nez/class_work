import sys
sys.setrecursionlimit(8000)

def f(n):
    if n >= 7777:
        return n
    return n + 5 + f(n+5)

print(f(1101) - f(1111))