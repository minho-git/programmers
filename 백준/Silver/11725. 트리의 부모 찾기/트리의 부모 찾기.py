def dfs(v):
    # dfs 할때마다 result에 각 노드를 추가한다.
    visited[v] = True

    for next in graph[v]:
        if not visited[next]:
            dfs(next)
            answer[next] = v

import sys
sys.setrecursionlimit(10 ** 6)
N = int(input())

# 인접 리스트를 만든다.
graph = [[] for i in range(N + 1)]
answer = [0] * (N + 1)
visited =[False] * (N + 1)

# 인접 리스트를 입력받는다.
for i in range(N-1):
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append(end)
    graph[end].append(start)


# 루트 노드가 1이므로, 1부터 시작해서 dfs를 시작한다.
dfs(1)

for i in range(2, N+1):
    print(answer[i])