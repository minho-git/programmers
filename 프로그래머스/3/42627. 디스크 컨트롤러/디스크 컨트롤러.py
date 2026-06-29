import heapq

def solution(jobs):
    jobs.sort()
    i = 0
    now = 0
    answer = 0
    heap = []
    
    while i < len(jobs) or heap:
        while i < len(jobs) and jobs[i][0] <= now:
            tmp = [jobs[i][1], jobs[i][0], i]
            heapq.heappush(heap, tmp)
            i += 1
        
        if heap:
            popped = heapq.heappop(heap)
            now += popped[0]
            answer += now - popped[1]

        else:
            now = jobs[i][0]
        
    return answer // len(jobs)