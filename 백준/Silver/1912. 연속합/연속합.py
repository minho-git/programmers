n = int(input())


lst = list(map(int, input().split()))
lst.insert(0, 0)
dp = [0 for i in range(n+1)]
answer = lst[1]

for i in range(1, len(lst)):
    if lst[i] < -dp[i-1]:
        dp[i] = 0

    else:
        dp[i] = dp[i-1] + lst[i]

    if answer > 0:
        answer = max(answer, dp[i])
    else:
        answer = max(answer, lst[i])

print(answer)






