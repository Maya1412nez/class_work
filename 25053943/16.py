import sys
sys.setrecursionlimit(20000)

def f(n):
    if n >= 15000:
        return n - 14500
    if 5000 < n < 15000:
        return f(n+5) + 2 * n - 6
    if 500 < n <= 5000:
        return 3*n + f(n+3)
    if n <= 500:
        return n + f(n+1)
    
print(f(21))