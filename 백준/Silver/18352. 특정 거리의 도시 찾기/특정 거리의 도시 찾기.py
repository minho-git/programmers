import sys
from collections import deque

# N(노드 개수), M(에지 개수), K(목표 거리), X(시작점)
N, M, K, X = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
visited = [-1] * (N + 1) # 각 노드의 최소거리를 입력, -1일때는 방문X
answer = []

# BFS(시작점)
    # 큐를 만들고, 첫 번째 큐에 시작점을 대입
    # 초기 거리 설정

    # While 큐가 빌때까지:
        # 큐에서 하나 빼서
        # 방문할 수 있는 노드들을 반복하면서
        # 만약 뺀 값이 방문안했다면
        # 큐에 대입
        # 거리 설정(이전 값 이용)

def BFS(v):
    que = deque()
    que.append(v)
    visited[v] = 0

    while que:
        current_node = que.popleft()
        for next_node in graph[current_node]:
            if visited[next_node] == -1:
                que.append(next_node)
                visited[next_node] = visited[current_node] + 1


for i in range(M):
    A, B = map(int, sys.stdin.readline().split())
    graph[A].append(B)

# BFS() 시작
BFS(X)

for i in range(1, N+1):
    if visited[i] == K:
        answer.append(i)


if not answer:
    print(-1)
else:
    answer.sort()
    for i in answer:
        print(i)


