def dfs(src, tickets, visited, result):

    if len(result) == len(tickets) + 1:
        return result

    for index, ticket in enumerate(tickets):
        if not visited[index] and ticket[0] == src:
            visited[index] = True
            des = ticket[1]
            result.append(des)
            
            tmp = dfs(des, tickets, visited, result)
            if tmp:
                return tmp
            
            visited[index] = False
            result.pop()
            
def solution(tickets):    
    visited = [False] * len(tickets)
    tickets.sort(key=lambda x : (x[0], x[1]))
    
    answer = dfs("ICN", tickets, visited, ["ICN"])

    return answer