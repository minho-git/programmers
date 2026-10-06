def solution(s):
    
    _dict = {}
    _dict["zero"] = 0
    _dict["one"] = 1
    _dict["two"] = 2 
    _dict["three"] = 3 
    _dict["four"] = 4
    _dict["five"] = 5 
    _dict["six"] = 6
    _dict["seven"] = 7 
    _dict["eight"] = 8 
    _dict["nine"] = 9
    
    answer = []
    tmp = ""
    
    for c in s:
        if c.isdigit():
            if tmp:
                answer.append(_dict[tmp])
                tmp = ""
                
            answer.append(c)
            
        elif tmp in _dict:
            answer.append(_dict[tmp])
            tmp = c
        
        else:
            tmp += c
    
    
    if tmp:
        answer.append(_dict[tmp])
    
    
    
    
    result = 0
    
    for i in range(len(answer)):
        num = int(answer[i])
        result = result * 10 + num
    return result