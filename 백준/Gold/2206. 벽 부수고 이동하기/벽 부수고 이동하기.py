from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

N, M = map(int, input().split())

graph = []
for i in range(N):
    graph.append(list(map(int, input())))

# 일단 이동을 위한 큐가 필요하다.
q = deque()
q.append((0, 0, 1, 0))
visited = [[[float("inf")] * M for _ in range(N)] for __ in range(2)]
visited[1][0][0] = 1
visited[0][0][0] = 1

while q:
    y, x, dist, check = q.popleft()

    for i in range(4):
        yy = y + dy[i]
        xx = x + dx[i]
        new_dist = dist + 1

        if 0 <= yy < N and 0 <= xx < M:
            if check == 0:

                if graph[yy][xx] == 0 and visited[0][yy][xx] > new_dist:
                    q.append((yy, xx, new_dist, 0))
                    visited[0][yy][xx] = new_dist

                elif graph[yy][xx] == 1 and visited[1][yy][xx] > new_dist:
                    q.append((yy, xx, new_dist, 1))
                    visited[1][yy][xx] = new_dist

            else:
                if graph[yy][xx] == 0 and visited[1][yy][xx] > new_dist:
                    q.append((yy, xx, new_dist, 1))
                    visited[1][yy][xx] = new_dist


if visited[1][N-1][M-1] == float("inf") and visited[0][N-1][M-1] == float("inf"):
    print(-1)
else:
    print(min(visited[1][N-1][M-1], visited[0][N-1][M-1]))

