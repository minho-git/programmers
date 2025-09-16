import sys

stack = list()

k = int(input())

for i in range(k):
    num = int(sys.stdin.readline())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)


total = 0
for x in stack:
    total += x


print(total)