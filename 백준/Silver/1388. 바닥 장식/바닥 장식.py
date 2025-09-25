N, M = map(int, input().split())

graph = [[' ' for j in range(M+1)] for i in range(N+1)]

for i in range(1, N+1):
    board = " "+ input()
    for j in range(1, M+1):
        graph[i][j] = board[j]

count = 0

for i in range(1, N+1):
    for j in range(1, M):
        if graph[i][j] == "-" and graph[i][j+1] == '|':
            count += 1

    if graph[i][M] == '-':
        count += 1


for j in range(1, M + 1):
    for i in range(1, N):
        if graph[i][j] == '|' and graph[i+1][j] == '-':
            count += 1

    if graph[N][j] == '|':
        count += 1



print(count)



