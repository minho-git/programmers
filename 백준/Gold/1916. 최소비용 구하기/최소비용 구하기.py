import sys
import heapq

input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
dy = [float("inf")] * (N+1)

for i in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

start, end = map(int, input().split())

def dijkstra(s):
    q = [(0, s)]
    dy[s] = 0

    while q:
        dist, now = heapq.heappop(q)

        if dist > dy[now]:
            continue

        for next_node, next_dist in graph[now]:
            if dy[next_node] > dist + next_dist:
                dy[next_node] = dist + next_dist
                heapq.heappush(q, (dist + next_dist, next_node))

dijkstra(start)

print(dy[end])
