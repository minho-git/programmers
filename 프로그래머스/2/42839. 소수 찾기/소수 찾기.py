def dfs(index, numbers, visited, result, _set):
    
    if result not in ["", "1", "0"]:
        _set.add(int(result))
    
    for num in numbers:
        if num in visited:
            if visited[num] == 1:
                del visited[num]
                
            else:
                visited[num] -= 1  
                
            dfs(index+1, numbers, visited, result + num, _set)
            visited[num] = visited.get(num, 0) + 1
            
    
def check(num):
    if num < 2:
        return False
    
    for i in range(2, num):
        if num % i == 0:
            return False
    else:
        return True        
    

def solution(numbers):
    answer = 0
    _set = set()
    _dict = {}
    
    for num in numbers:
        _dict[num] = _dict.get(num, 0) + 1
    
    dfs(0, numbers, _dict, "", _set)
    print(_set)
    
    for num in _set:
        print(num)
        if check(int(num)):
            answer += 1
    
    return answer