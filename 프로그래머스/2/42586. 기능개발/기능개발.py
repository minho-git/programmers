from collections import deque

def solution(progresses, speeds):
    q = deque()
    day = 0
    answer = []
    
    for i, progress in enumerate(progresses):
        q.append((i, progress))
    
    
    while q:
        count = 1
        index, current = q.popleft()
        current += day * speeds[index]
        
        while current < 100:
            day += 1
            current += speeds[index]
        
        while q:
            next = q.popleft()
            if next[1] + speeds[next[0]] * day >= 100:
                count += 1
            else:
                q.appendleft(next)
                break
                
        
        answer.append(count)
        
    
    return answer