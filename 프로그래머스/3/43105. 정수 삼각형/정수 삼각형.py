def solution(triangle):
    answer = 0
    dp = []
    
    for i in range(len(triangle)):
        dp.append([0] * len(triangle[i]))
        
    
    for i in range(len(triangle)):
        for j in range(len(triangle[i])):
            tmp = 0
            
            if i == 0:
                tmp = triangle[0][0]
                dp[0][0] = tmp
                
            elif j == 0:
                tmp = dp[i-1][0] + triangle[i][0]
                dp[i][0] = tmp
                
            elif j == i:
                tmp = dp[i-1][i-1] + triangle[i][j]
                dp[i][j] = tmp
                
            else:
                tmp = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
                dp[i][j] = tmp
            
            if tmp > answer:
                answer = tmp
                
    
    return answer