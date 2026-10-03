def solution(arr):
    answer = []
    
    if len(arr) == 1:
        answer.append(-1)
        
    _min = min(arr)
    
    for num in arr:
        if _min != num:
            answer.append(num)
    
    return answer