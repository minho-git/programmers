def solution(phone_book):
    _dict = {i : dict() for i in range(1, 21)}
    
    for i in range(len(phone_book)):
        for j in range(1, len(phone_book[i]) + 1):
            _dict[j][(phone_book[i][:j])] = _dict[j].get((phone_book[i][:j]), 0) + 1
    
    
    
    for i in range(len(phone_book)):
        tmp = phone_book[i]
        if _dict[len(tmp)].get(tmp, 0) > 1:
            return False
            
    
    return True