import sys
sys.setrecursionlimit(6000)

def f(n):
    if n == 1: return 1
    if n > 1:
        return (n+1) * f(n-1)
print(f(5037) / f(5034))