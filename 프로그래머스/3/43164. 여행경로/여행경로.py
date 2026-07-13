def solution(tickets):
    answer = 0
    visited = [False] * len(tickets)
    tickets.sort()
    
    def dfs(start, result):
        if len(result) == len(tickets) + 1:
            return result
        
        for index, ticket in enumerate(tickets):
            if not visited[index] and ticket[0] == start:
                visited[index] = True
                result.append(ticket[1])
                tmp = dfs(ticket[1], result)
                if tmp:
                    return result
                
                visited[index] = False
                result.pop()
                
    answer = dfs("ICN", ["ICN"])
    
    return answer