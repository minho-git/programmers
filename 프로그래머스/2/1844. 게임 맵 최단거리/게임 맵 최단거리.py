from collections import deque

def solution(maps):
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    
    n = len(maps)
    m = len(maps[0])
    
    q = deque()
    q.append((0, 0, 1))
    maps[0][0] = -1
    
    
    while q:
        
        popped = q.popleft()
        y = popped[0]
        x = popped[1]
        level = popped[2]
        
        print(y, x, level)
        
        if  y == n-1 and x == m-1:
            return level
        
        for i in range(4):
            new_y = y + dy[i]
            new_x = x + dx[i]
            
            if n > new_y >= 0 and m > new_x >= 0 and maps[new_y][new_x] == 1:
                q.append((new_y, new_x, level + 1))
                maps[new_y][new_x] = -1
        
        
    return -1