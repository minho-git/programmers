def solution(m, n, puddles):
    answer = 0
    dp = [[0] * (n+2) for _ in range(m+2)]

    for y, x in puddles:
        dp[y][x] = -1
        

    for i in range(1, m+1):
        for j in range(1, n+1):
            if dp[i][j] == -1:
                pass
            else:
                if i == 1 and j == 1:
                    dp[i][j] = 1

                else:
                    
                    if dp[i-1][j] == -1 and dp[i][j-1] == -1:
                        pass
                    elif dp[i-1][j] == -1:
                        dp[i][j] = dp[i][j-1]
                    elif dp[i][j-1] == -1:
                        dp[i][j] = dp[i-1][j]
                    else:
                        dp[i][j] = dp[i-1][j] + dp[i][j-1]
                
                
                
    answer = dp[i][j] % 1000000007
    return answer