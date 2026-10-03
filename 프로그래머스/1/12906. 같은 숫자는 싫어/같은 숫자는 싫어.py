def solution(arr):
    answer = []
    
    for number in arr:
        if not answer:
            answer.append(number)
        
        if answer[-1] != number:
            answer.append(number)
        
            
            
    return answer