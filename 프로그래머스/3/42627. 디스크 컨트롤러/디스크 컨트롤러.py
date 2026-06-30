import heapq

def solution(jobs):
    jobs.sort()
    heap = []
    answer = 0
    time = 0
    i = 0
    
    while i < len(jobs) or heap:
        
        while i < len(jobs) and jobs[i][0] <= time:
            소요시간 = jobs[i][1]
            요청시간 = jobs[i][0]
            tmp = [소요시간, 요청시간, i]
            heapq.heappush(heap, tmp)
            i += 1
        
        if heap:
            popped = heapq.heappop(heap)
            time += popped[0]
            answer += time - popped[1]
        
        else:
            time = jobs[i][0]
        
    return answer // len(jobs)