def check(s):
    tmp = list()
    
    for i in s:
        if i in ["(", "{", "["]:
            tmp.append(i)
        else:
            if not tmp:
                return False
            elif i == ")":
                if tmp[-1] == "(":
                    tmp.pop()
            elif i == "}":
                if tmp[-1] == "{":
                    tmp.pop()
            elif i == "]":
                if tmp[-1] == "[":
                    tmp.pop()
        
    
    if tmp:
        return False
    else:
        return True
                
                

def solution(s):
    answer = 0
    
    for i in range(len(s)):
        # 새로운 문자열 만들기
        new_s = s[i:] + s[:i]
        
        # 문자열 체크 함수 호출하기
        if check(new_s):
            answer += 1

    return answer

