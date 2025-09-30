# 교차 한다 ? -> 전깃줄 A의 위치와 B의 위치가 순차적 으로 커져야 한다.
# 전깃줄 A의 1번 위치인 경우 B의 위치는 전깃줄 A의 3번 위치인 경우 B의 위치 보다 작아야 한다.

# 8
# 1 8
# 3 9
# 2 2
# 4 1
# 6 4
# 10 10
# 9 7
# 7 6

n = int(input())
lines = []
count = 0

for i in range(n):
    start, end = map(int, input().split())
    lines.append((start, end))

lines.sort(key=lambda x:x[0])
removed_list = [False for i in range(n)]

lst = [0]

for i in range(n):
    lst.append(lines[i][1])

dp = [0 for i in range(n+1)]
dp[1] = 1

for i in range(2, n+1):
    for j in range(i-1, 0, -1):
        if lst[i] > lst[j]:
            dp[i] = max(dp[i], dp[j])

    dp[i] += 1

print(n - max(dp))