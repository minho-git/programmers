n = int(input())

dp = [[0 for i in range(10)] for j in range(n+1)]
result = 0

for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, n+1):
    dp[i][0] = dp[i-1][1]
    dp[i][9] = dp[i-1][8]

    for j in range(1, 9):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

for i in range(0, 10):
    result += dp[n][i]


print(result % 1000000000)



