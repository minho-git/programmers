import sys
from collections import deque

N = int(input())

graph = [[0 for i in range(N+1)]]
dp = [[0 for i in range(N+1)] for j in range(N+1)]
dp[1][1] = 1


for i in range(1, N+1):
    graph.append(list(map(int, sys.stdin.readline().split())))
    graph[i].insert(0, 0)



for i in range(1, N+1):
    for j in range(1, N+1):
        value = graph[i][j]

        if value == 0:
            continue

        if j + value <= N:
            dp[i][j + value] += dp[i][j]

        if i + value <= N:
            dp[i + value][j] += dp[i][j]


print(dp[N][N])



