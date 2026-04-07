arr1 = list(input())
arr2 = list(input())

arr1.insert(0, "X")
arr2.insert(0, "X")


dp = [[0] * (len(arr2)) for _ in range(len(arr1))]

for i in range(1, len(arr1)): # 길이가 이미 늘어났음!!
    for j in range(1, len(arr2)):
        if arr1[i] == arr2[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])


answer = 0
for i in range(1, len(dp)):
    for j in range(1, len(dp[i])):
        if answer < dp[i][j]:
            answer = dp[i][j]

print(answer)