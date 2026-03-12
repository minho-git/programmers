def solution(s):
    res = ""

    if s[0].isdigit():
        res += s[0]
    elif s[0].isalpha():
        res += s[0].upper()
    else:
        res += s[0]
        
    
    for i in range(1, len(s)):
        if s[i-1] == " ":
            if s[i].isdigit():
                res += s[i]
            elif s[i].isalpha():
                res += s[i].upper()
            else:
                res += s[i]
        else:
            res += s[i].lower()        
            
    return res