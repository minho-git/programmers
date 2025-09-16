def multi(a, b, c):

    if b == 1:
        return a % c

    tmp = multi(a, b // 2, c)
    if (b % 2) == 0:
        return (tmp * tmp) % c
    else:
        return (multi(a, (b // 2) + 1, c) * tmp) % c



A, B, C = map(int, input().split())

print(multi(A, B, C))