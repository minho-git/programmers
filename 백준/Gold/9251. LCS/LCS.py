#    0  A  C  A  Y  K  P
# 0  0  0  0  0  0  0  0
# C  0  0  1  1  1  1  1
# A  0  1  1  2  2  2  2
# P  0  1  1  2  2  2  3
# C  0  1  2  2  2  2  3
# A  0  1  2  3  3  3  3
# K  0  1  2  3  3  4  4


str1 = " " + input()
str2 = " " + input()


dp = [[0 for i in range(len(str1) + 1)] for j in range(len(str2) + 1)]

for i in range(1, len(str2)):
    for j in range(1, len(str1)):
        if str2[i] == str1[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

answer = 0
for i in range(1, len(dp)):
    for j in range(1, len(dp[0])):
        answer = max(answer, dp[i][j])

print(answer)