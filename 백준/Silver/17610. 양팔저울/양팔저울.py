import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

K = int(input())
arr = []

arr += list(map(int, input().split()))

total = sum(arr)
check = [0] * (total + 1)
res = 0

def dfs(level, _sum):

    if level == K:
        if 0 < _sum <= total:
            check[_sum] = 1

    else:
        dfs(level + 1, _sum + arr[level])
        dfs(level + 1, _sum - arr[level])
        dfs(level + 1, _sum)


dfs(0, 0)

for i in range(1,total+1):
    if check[i] == 0:
        res += 1

print(res)