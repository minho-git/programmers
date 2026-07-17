import heapq, sys

def solution(N, road, K):
    answer = 0
    graph = [[] for _ in range(N+1)]
    dist = [int(1e9)] * (N+1)
    dist[1] = 0
    
    for r in road:
        graph[r[0]].append((r[2], r[1]))
        graph[r[1]].append((r[2], r[0]))
    
    q = [(0, 1)] # (가중치, 다음 노드)
    
    while q:
        popped = heapq.heappop(q)
        value = popped[0]
        node = popped[1]
        
        for v in graph[node]:
            tmp = value + v[0]
            if tmp < dist[v[1]]:
                dist[v[1]] = tmp
                heapq.heappush(q, (tmp, v[1]))
        
    
    for d in dist:
        if d <= K:
            answer += 1
    
    
    
    return answer