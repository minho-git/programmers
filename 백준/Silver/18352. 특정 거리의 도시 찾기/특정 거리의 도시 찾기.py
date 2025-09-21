import sys
from collections import deque

N, M, K, X = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
distance = [-1] * (N + 1)

for i in range(M):
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append((end, 0))

que = deque()
que.append((X, 0))
distance[X] = 0
answer = []

while que:

    방문도시, 횟수 = que.popleft()

    if 횟수 == K:
        answer.append(방문도시)

    elif 횟수 < K:
        for 방문할도시, _ in graph[방문도시]:
            if distance[방문할도시] == -1:
                que.append((방문할도시, 횟수 + 1))
                distance[방문할도시] = 횟수+1


answer.sort()

if not answer:
    print(-1)
else:
    for i in answer:
        print(i)


