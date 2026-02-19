s = input()
stack = []
res = ""

for x in s:
    if x.isalpha():
        res += x
    else:
        if x == '(':
            stack.append('(')

        elif x in ["*", "/"]:
            while stack and stack[-1] in ["*", "/"]:
                res += stack.pop()
            stack.append(x)

        elif x in ["+", "-"]:
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.append(x)

        elif x == ")":
            while stack and stack[-1] != '(':
                res += stack.pop()

            stack.pop()

while stack:
    res += stack.pop()


print(res)