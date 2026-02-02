import math

def solution(n):
    answer = 0
    
    for i in range(1, math.ceil(math.sqrt(n))):
        if n % i == 0:
            answer += 2
            
    if n % math.sqrt(n) == 0:
        answer += 1
    
    return answer