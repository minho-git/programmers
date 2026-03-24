def check(s):
    tmp = list(s)
    stack = []
    while tmp:
        _popped = tmp.pop()
        if _popped in (")", "}", "]"):
            stack.append(_popped)
        else:
            if len(stack) == 0:
                return False
            
            if _popped == "(":
                if stack.pop() == ")":
                    continue
                else:
                    return False
            elif _popped == "{":
                if stack.pop() == "}":
                    continue
                else:
                    return False
            elif _popped == "[":
                if stack.pop() == "]":
                    continue
                else:
                    return False
                
    if len(stack) > 0:
        return False
    else:
        return True
    
def solution(s):
    answer = 0
    
    for i in range(len(s)):
        tmp = s[i:len(s)] + s[0:i]
        if check(tmp):
            answer += 1
            
    
    return answer