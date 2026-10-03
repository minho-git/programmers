def solution(s, n):
    answer = []
    
    for c in s:
        if c == " ":
            answer.append(" ")
            continue
        
        tmp = ord(c) + n
        if c.isupper():
            if tmp > 90:
                tmp -= 26
            
        else:
            if tmp > 122:
                tmp -= 26
            
        answer.append(chr(tmp))

    return "".join(answer)