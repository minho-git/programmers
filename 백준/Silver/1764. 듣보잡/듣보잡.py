N, M = map(int, input().split())
arr = set()
res = 0
result = []
# set은 add
for i in range(N):
    arr.add(input())

for i in range(M):
    tmp = input()

    if tmp in arr:
        res += 1
        result.append(tmp)

print(res)
result.sort()
for x in result:
    print(x)
