# 도시 개수
import sys

n = int(input())

# 버스 개수
m = int(input())

# 인접 행렬(n * n) 초기화 및 같은 좌표 0으로 초기화
adj_lst = [[sys.maxsize for i in range(n+1)] for j in range(n+1)]

for i in range(1, n + 1):
    adj_lst[i][i] = 0

# 버스 입력 받기
for i in range(m):
    start, end, weight = map(int, sys.stdin.readline().split())
    if adj_lst[start][end] == sys.maxsize:
        adj_lst[start][end] = weight
    else:
        adj_lst[start][end] = min(adj_lst[start][end], weight)


# 플로이드-워셜 알고리즘 진행
for k in range(1, n+1):
    for s in range(1, n+1):
        for e in range(1, n+1):
            adj_lst[s][e] = min(adj_lst[s][e], adj_lst[s][k] + adj_lst[k][e])


for i in range(1, n+1):
    for j in range(1, n+1):
        if adj_lst[i][j] == sys.maxsize:
            print(0, end=" ")
        else:
            print(adj_lst[i][j], end=" ")
    print()

