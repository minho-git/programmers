lst = list(input())
bomb = list(input())

stack = []

for i in range(len(lst)):
    stack.append(lst[i])

    if len(stack) >= len(bomb):
        if stack[-len(bomb):] == bomb:
            for j in range(len(bomb)):
                stack.pop()


if stack:
    print(''.join(stack))
else:
    print("FRULA")

