def separate(string):
    open_count = 0
    close_count = 0

    for i in range(len(string)):
        if string[i] == '(':
            open_count += 1
        else:
            close_count += 1

        if open_count == close_count:
            return string[0 : i + 1], string[i + 1:]

def is_correct_string(string):
    stack = []

    for char in string:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if len(stack) == 0:
                return False
            else:
                stack.pop()

    return len(stack) == 0


def solution(balanced_parentheses_string):
    if not balanced_parentheses_string:
        return ""

    (u, v) = separate(balanced_parentheses_string)

    if is_correct_string(u):
        v = solution(v)
        u = u + v
        return u
    else:
        empty_string = "("

        empty_string += solution(v)

        empty_string += ')'

        u = u[1:-1]
        tmp = ""
        for i in range(len(u)):
            if u[i] == '(':
                tmp += ')'
            else:
                tmp += '('

        empty_string += tmp

        return empty_string