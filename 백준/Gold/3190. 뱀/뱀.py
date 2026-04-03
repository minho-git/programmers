from collections import deque

N = int(input())
K = int(input())
graph = [[0] * N for _ in range(N)]
graph[0][0] = -1 # -1은 몸, 1은 사과

for i in range(K):
    y, x = tuple(map(int, input().split()))
    graph[y-1][x-1] = 1 # 1이면 사과

L = int(input())
time_line = [] # [시간, 방향], 'L' -> 왼쪽 90도, 'D' -> 오른쪽 90도
for i in range(L):
    time_line.append(tuple(input().split()))

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

tail = [0, 0]
head = [0, 0]
now = 0
d = 1
next_time, direction = time_line.pop(0)

q = deque()

while True:
    now += 1

    head[0] += dy[d]
    head[1] += dx[d]
    q.append(d)

    # 벽을 만났을때
    if head[0] < 0 or head[0] >= N or head[1] < 0 or head[1] >= N:
        break

    # 몸과 붙이쳤을때
    if graph[head[0]][head[1]] == -1:
        break

    # 사과가 있었을때
    if graph[head[0]][head[1]] == 1:
        graph[head[0]][head[1]] = -1

    # 사과가 없었을때
    else:
        graph[head[0]][head[1]] = -1 # 머리가 이동했으니깐 무조건 -1로 해줘야함. 사과가 있든 없든
        graph[tail[0]][tail[1]] = 0
        next_d = q.popleft()

        tail[0] += dy[next_d]
        tail[1] += dx[next_d]

    # 방향 전환 시간이 되었을 때
    if now == int(next_time):
        if direction == "D":
            d = (d+1) % 4
        else:
            d = (d+3) % 4

        if time_line:
            next_time, direction = time_line.pop(0)

print(now)