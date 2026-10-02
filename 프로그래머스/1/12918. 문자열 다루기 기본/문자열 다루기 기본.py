def solution(s):
    
    s_len = len(s)
    
    if s_len not in (4, 6):
        return False
    
    for c in s:
        if not c.isdigit():
            return False
    
    
    return True