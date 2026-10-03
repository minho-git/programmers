def solution(s, n):
    answer = []
    
    
    for c in s:
        if c == " ":
            answer.append(" ")
            continue
        
        tmp = ord(c)
        if c.isupper():
            tmp += n
            
            if tmp > 90:
                tmp -= 26
            
            answer.append(chr(tmp))
            
        else:
            tmp += n
            
            if tmp > 122:
                tmp -= 26
            
            answer.append(chr(tmp))

    return "".join(answer)