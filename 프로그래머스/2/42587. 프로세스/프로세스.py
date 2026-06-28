from collections import deque

def solution(priorities, location):
    
    q = deque()
    count = 0
    answer = 0
    
    for i in range(len(priorities)):
        q.append((i, priorities[i]))
    
    
    while q:
        popped = q.popleft()
        
        for i, j in q:
            if popped[1] < j:
                q.append(popped)
                break
        else:
            count += 1
            if popped[0] == location:
                answer = count
        
    return answer