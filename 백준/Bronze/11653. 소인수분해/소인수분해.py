N = int(input())

if N == 1:
    pass
else:
    D = 2

    while (D * D <= N):
        while (N % D == 0):
            print(D)
            N //= D
        
        D += 1

if N > 1:
        print(N)

    