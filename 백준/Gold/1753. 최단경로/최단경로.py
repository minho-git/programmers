import sys
import heapq

input = lambda : sys.stdin.readline().rstrip()

V, E = map(int, input().split())
K = int(input())

graph = [[] for _ in range(V+1)] # 크기가 클때 연결 리스트 사용하기!

for i in range(E):
    u, v, w = tuple(map(int, input().split()))
    graph[u].append((v, w))

distance = [float("inf")] * (V+1)
distance[K] = 0

q = [(0, K)] # (가중치, 노드) # 힙에는 앞에 요소가 정렬 대상!

while q:

    price, node = heapq.heappop(q)

    if distance[node] < price: # 큐에 남아있는 비싼 쓰레기 버리기
        continue

    for next_node, next_price in graph[node]:

        total = price + next_price
        if distance[next_node] > total:
            heapq.heappush(q, (total, next_node))
            distance[next_node] = total

for i in range(1, len(distance)):
    if distance[i] == float("inf"):
        print("INF")
    else:
        print(distance[i])
