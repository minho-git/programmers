import sys

N, K = map(int, input().split())

coins = []
count = 0

for i in range(N):
    coins.append(int(sys.stdin.readline()))

coins.reverse()

for coin in coins:
    if K == 0:
        break

    if K >= coin:

        count+= K//coin

        K %= coin


print(count)
