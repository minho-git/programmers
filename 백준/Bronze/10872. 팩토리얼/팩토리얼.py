from math import factorial

N = int(input())
if N == 0:
    print(1)
else:

    print(factorial(N))

def factorial(n):
    if n == 1:
        return 1

    else:
        return n * factorial(n-1)