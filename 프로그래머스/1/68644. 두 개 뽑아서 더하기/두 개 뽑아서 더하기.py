def solution(numbers):
    answer = set()
    
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            tmp = numbers[i] + numbers[j]
            answer.add(tmp)
            
    
    answer = list(answer)
    answer.sort()
    
    return answer