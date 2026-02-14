# 그리디 문제는 정렬이 동반된다.

N = int(input())
arr = []
for i in range(N):
    s, e = map(int, input().split())
    arr.append((s, e))

arr.sort(key=lambda x : (x[1], x[0]))

res = 1
cur = arr[0]

for i in range(1, N):
    if arr[i][0] >= cur[1]:
        res += 1
        cur = arr[i]

print(res)