def solution(string):
    
    stack = []

    for char in string:
        if len(stack) == 0:
            if char == '(':
                stack.append(char)
                continue
            else:
                return False
        else:
            if char == '(':
                stack.append(char)
            else:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    return False


    return len(stack) == 0
    