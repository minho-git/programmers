import heapq

def solution(n, s, a, b, fares):

    # n: 지점의 갯수
    # s: 출발지
    # a,b: 각 도착지점
    
    # 중간 노드 마다 다익스트라 알고리즘을 사용해서 계산하자.
    # 중간노드를 k로 한다면.
    # k에서 출발해서 모든 노드의 비용을 구한다.
    # 이후 k to A, k to B, k to s를 다 구해서 더한다.
    # 그리고 이걸 어디에 저장한다.
    # 이걸 각 노드마다 반복해서 제일 작은게 정답.
    answer = int(1e9)
    graph = [[] for _ in range(n+1)]
    for fare in fares:
        graph[fare[0]].append((fare[2], fare[1]))
        graph[fare[1]].append((fare[2], fare[0]))

    for i in range(1, n+1):
        
        visited = [int(1e9)] * (n+1)
        q = [(0, i)]
        visited[i] = 0
        
        while q:
            popped = heapq.heappop(q)
            value = popped[0]
            node = popped[1]
            
            for next_cost, next_node in graph[node]:
                tmp = visited[node] + next_cost
                if tmp < visited[next_node]:
                    visited[next_node] = tmp
                    heapq.heappush(q, (tmp, next_node))
            
        total = visited[s] + visited[a] + visited[b]
        
        if total < answer:
            answer = total
    
    return answer