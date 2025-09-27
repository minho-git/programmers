N = int(input())
plan = [(0,0)]
dp = [0 for i in range(100)]

for i in range(N):
    t, p = map(int, input().split())

    plan.append((t, p))

for i in range(1, N+1):

    dp[i + plan[i][0]] = max(dp[i + plan[i][0]], dp[i] + plan[i][1])

    dp[i+1] = max(dp[i+1], dp[i])


print(dp[N+1])