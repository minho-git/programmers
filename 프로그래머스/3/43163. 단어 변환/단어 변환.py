from collections import deque

def solution(begin, target, words):
    answer = 0
    q = deque()
    visited = [False] * len(words)
    
    q.append((begin, 0))
    
    while q:
        
        popped = q.popleft()
        a = popped[0]
        level = popped[1]
        
        if a == target:
            return level
        
        
        for i in range(len(visited)):
            
            if not visited[i]:
                b = words[i]

                for j in range(len(words[i])):
                    if a[:j] == b[:j] and a[j+1:] == b[j+1:]:
                        q.append((b, level + 1))
                        visited[i] = True
                    
    
    return 0