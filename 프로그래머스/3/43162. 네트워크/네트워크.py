def dfs(y, x, visited, computers):
    
    for i in range(len(computers)):
        if computers[x][i] == 1 and visited[x][i] == 0:
            visited[x][i] = 1
            dfs(x, i, visited, computers)
            
    

def solution(n, computers):
    answer = 0
    visited = [(n) * [0] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
        
            if computers[i][j] == 1 and visited[i][j] == 0:
                dfs(i, j, visited, computers)
                answer += 1

    return answer