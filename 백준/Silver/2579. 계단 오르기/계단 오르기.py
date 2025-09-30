n = int(input())
stairs = [0] * (n + 1)
for i in range(1, n + 1):
    stairs[i] = int(input())

# (n이 1이나 2일 수도 있으니 예외 처리를 해주는 것이 좋습니다)
if n == 1:
    print(stairs[1])
else:
    dp = [0] * (n + 1)
    dp[1] = stairs[1]
    dp[2] = stairs[1] + stairs[2]

    for i in range(3, n + 1):
        # 직접 완성하신 완벽한 점화식!
        dp[i] = max(stairs[i - 1] + dp[i - 3] + stairs[i], dp[i - 2] + stairs[i])

    # 마지막 계단은 반드시 밟아야 하므로 dp[n]이 정답입니다.
    print(dp[n])