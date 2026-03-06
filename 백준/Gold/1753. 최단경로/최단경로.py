import heapq
import sys

# 입력 속도 향상 (필수)
input = sys.stdin.readline

V, E = map(int,input().split())
K = int(input())

graph = [[] for _ in range(V+1)]
dy = [float("inf")] * (V+1)

for i in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

def dijkstra(start):
    q = [(0, start)] # 이거 첫 번째 요소로 정렬됨!!
    dy[start] = 0

    while q:
        value, now = heapq.heappop(q)

        if dy[now] < value:
            continue

        for next_node, weight in graph[now]:
            if dy[next_node] > value + weight:
                dy[next_node] = value + weight
                heapq.heappush(q, (value + weight, next_node))

dijkstra(K)

for i in range(1, len(dy)):
    if dy[i] == float("inf"):
        print("INF")
    else:
        print(dy[i])