from math import ceil

A, B, V = map(int, input().split())

tmp = (V - A) / (A - B)
if 0 < tmp < 1:
    print(2)
elif tmp == 0:
    print(1)
else:
    print(ceil(tmp) + 1)
