def dfs(index, result, array, value):
    
    if index == len(array):
        if result == value:
            return 1
    
        return 0
    
    
    # 각 인덱스의 있는 값을 더하거나 빼거나 한다.
    return dfs(index+1, result + array[index], array, value) + dfs(index+1, result - array[index], array, value)

def solution(numbers, target): 
    
    answer = dfs(0, 0, numbers, target)

    return answer