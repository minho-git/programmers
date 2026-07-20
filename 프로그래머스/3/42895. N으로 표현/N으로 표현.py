def solution(N, number):
    
    # dp[i] = N을 i번 사용해서 만들 수 있는 모든 숫자의 집합(set)
    # dp[k] = dp[i] op dp[k-i]
    
    # dp[1] = {5}
    # dp[2] = {55} U dp[1] op dp[1]
    # dp[3] = {555} U dp[1] op dp[2] or dp[2] op dp[1]
    
    dp = [set() for _ in range(9)]
    dp[1].add(N)
    
    if number == N:
        return 1
    
    for i in range(2, 9):
        for k in range(1, i):
            dp[i].add(int(str(N) * i))

            
            for num1 in dp[k]:
                for num2 in dp[i-k]:
                    dp[i].add(num1 + num2)
                    dp[i].add(num1 - num2)
                    dp[i].add(num1 * num2)
                    if num2 != 0:
                        dp[i].add(num1 // num2)
                    
            
        if number in dp[i]:
            return i
    
    return -1