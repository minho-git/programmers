from collections import Counter

def solution(clothes):
    
    count = Counter([kind for _, kind in clothes]) # dict처럼 사용 가능
    
    result = 1
    for value in count.values():
        result *= (value + 1)
        
    
    return result - 1