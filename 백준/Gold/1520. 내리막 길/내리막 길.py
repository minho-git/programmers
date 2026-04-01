import sys

sys.setrecursionlimit(10**6)

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

M, N = map(int, input().split())
graph = []
dp = [[-1] * N for _ in range(M)]

for i in range(M):
    graph.append(list(map(int, input().split())))

def dfs(y, x):
    if y == M-1 and x == N-1:
        return 1

    if dp[y][x] != -1:
        return dp[y][x]

    dp[y][x] = 0

    for i in range(4):
        yy = y + dy[i]
        xx = x + dx[i]

        if 0 <= yy < M and 0 <= xx < N and graph[yy][xx] < graph[y][x]:
            dp[y][x] += dfs(yy, xx) # 여기서 네 방향 중 끝에 도달한게 있으면 더한다.

    return dp[y][x] # 더한 결과를 이전 칸에 결과를 반영한다.

answer = dfs(0, 0)
print(answer)