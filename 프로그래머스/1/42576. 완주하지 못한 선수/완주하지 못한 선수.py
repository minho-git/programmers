def solution(participant, completion):
    _dict = dict()
    
    for p in participant:
        _dict[p] = _dict.get(p, 0) + 1
        
    
    for c in completion:
        if _dict.get(c, 1) == 1:
            _dict.pop(c)
        else:
            _dict[c] = _dict[c] - 1
    
    
    answer = list(_dict.keys())[0]
            
    
    
    return answer