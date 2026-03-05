n, k = map(int, input().split())
arr = []
for i in range(n):
    arr.append(int(input()))

dy = [float("inf")] * (k+1)
dy[0] = 0

for i in range(len(arr)):
    for j in range(arr[i], k+1):
        dy[j] = min(dy[j], dy[j-arr[i]] + 1)

if dy[k] == float("inf"):
    print(-1)
else:
    print(dy[k])
