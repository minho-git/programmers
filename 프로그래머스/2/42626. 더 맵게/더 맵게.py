import heapq

def solution(scoville, K):
    
    answer = 0
    scoville.sort()
    
    while True:
        if scoville[0] >= K:
            return answer
        
        if len(scoville) < 2:
            break
        
        _min_1 = heapq.heappop(scoville)
        _min_2 = heapq.heappop(scoville)
        new = _min_1 + 2 * _min_2
        heapq.heappush(scoville, new)
        answer += 1
        
        
    return -1