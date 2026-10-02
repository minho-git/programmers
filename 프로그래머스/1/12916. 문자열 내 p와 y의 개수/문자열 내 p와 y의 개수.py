def solution(s):
    s = s.lower()
    
    p = 0
    y = 0
    
    for c in s:
        if c == "p":
            p += 1
        elif c == "y":
            y += 1
    
    
    if p == y:
        return True

    return False