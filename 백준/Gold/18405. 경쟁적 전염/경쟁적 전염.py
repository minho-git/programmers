from collections import deque

N, K = map(int, input().split())
graph = []
que = deque()

for i in range(N):
    graph.append(list(map(int, input().split())))

S, X, Y = map(int, input().split())

for i in range(N):
    for j in range(N):
        if graph[i][j] != 0:
            que.append((graph[i][j], i, j))

que = deque(sorted(que, key=lambda x:x[0]))
time = 0

while time != S:

    if not que:
        break

    count = len(que)

    for i in range(count):
        popped = que.popleft()
        sort = popped[0]
        y = popped[1]
        x = popped[2]

        if 1 <= y < N and graph[y - 1][x] == 0:
            graph[y - 1][x] = graph[y][x]
            que.append((sort, y - 1, x))

        if y < N - 1 and graph[y + 1][x] == 0:
            graph[y + 1][x] = graph[y][x]
            que.append((sort, y + 1, x))

        if 1 <= x < N and graph[y][x - 1] == 0:
            graph[y][x - 1] = graph[y][x]
            que.append((sort, y, x - 1))

        if x < N - 1 and graph[y][x + 1] == 0:
            graph[y][x + 1] = graph[y][x]
            que.append((sort, y, x + 1))

    time += 1

print(graph[X-1][Y-1])