def dfs(y, visited, computers):
    
    for i in range(len(computers)):
        if computers[y][i] == 1 and visited[i] == 0:
            visited[i] = 1
            dfs(i, visited, computers)
            
    

def solution(n, computers):
    answer = 0
    visited = n * [0]
    
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and visited[j] == 0:
                visited[j] = 1
                dfs(j, visited, computers)
                answer += 1

    return answer