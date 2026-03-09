import sys
sys.setrecursionlimit(10**6)


N = int(input())

graph = []
res = 0
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
arr = []

for i in range(N):
    graph.append(list(map(int, input())))

def dfs(y, x, n):
    for k in range(4):
        yy = y +dy[k]
        xx = x +dx[k]

        if 0 <= yy < N and 0 <= xx < N and graph[yy][xx] == 1:
            arr[n] += 1
            graph[yy][xx] = 0
            dfs(yy, xx, n)


for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            graph[i][j] = 0
            arr.append(1)
            dfs(i, j,res)
            res += 1

arr.sort()
print(res)

for num in arr:
    print(num)

