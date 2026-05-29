def solution(clothes):
    _dict= {}
    result = 1
    
    for cloth in clothes:
        _dict[cloth[1]] = _dict.get(cloth[1], 0) + 1
    
    
    for key, value in _dict.items(): # items 기억안남.. enurmerate랑 헷갈림
        result *= (value + 1)
        
    return result - 1