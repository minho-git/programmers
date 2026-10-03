def solution(s):
    answer = ''
    count = 0
    
    for i in range(len(s)):
        if s[i] == " ":
            count = 0
            answer += " "
        elif count % 2 == 0:
            answer += s[i].upper()
            count += 1
        else:
            answer += s[i].lower()
            count += 1
        
    
    return answer