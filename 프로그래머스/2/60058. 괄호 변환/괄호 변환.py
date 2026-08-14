def check(s):
    stack = []
    
    for c in s:
        if c == "(":
            stack.append(c)
        elif c == ")":
            if not stack:
                return False
            elif stack[-1] == "(":
                stack.pop()
    
    if not stack:
        return True
            
    
def seperate(s):
    
    if not s:
        return ""
    
    open_count = 0
    close_count = 0
    index = 0
    v = ""
    
    for i in range(len(s)):
        
        if s[i] == "(":
            open_count += 1
        else:
            close_count += 1
        
        if open_count == close_count:
            index = i
            break
    
    u = s[:index+1]
    v = s[index+1:]
    v = seperate(v)
    
    if check(u):
        return u + v
    else:

        next = ""
        for i in range(len(u)):
            if u[i] == "(":
                next += ")"
            else:
                next += "("

        return "(" + v + ")" + next[1:-1]
            

def solution(balanced_parentheses_string):
    
    return seperate(balanced_parentheses_string)