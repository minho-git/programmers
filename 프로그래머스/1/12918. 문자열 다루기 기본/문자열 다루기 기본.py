def solution(s):
    
    s_len = len(s)
    
    if s_len not in (4, 6):
        return False
    
    for c in s:
        tmp = ord(c)
        
        if 48 > tmp or tmp > 57:
            return False
    
    
    return True