def solution(s):
    answer = []
    
    _dict = dict()
    
    for i in range(len(s)):
        c = s[i]
        
        if c not in _dict:
            answer.append(-1)
            _dict[c] = i
            
        else:
            answer.append(i - _dict[c])
            _dict[c] = i
            
        
    return answer